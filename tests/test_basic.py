import pytest
from unittest.mock import patch, MagicMock
from lmquickbench.cli import benchmark, main
import argparse

def test_benchmark_success():
    """Test the benchmark function with a mocked successful response."""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "usage": {"total_tokens": 100},
        "model": "mock-model",
        "choices": [{"message": {"content": "Mock output"}}],
    }

    with patch("requests.post", return_value=mock_response):
        result = benchmark("Test prompt", "http://mockserver.com", 256)
        assert result is not None
        assert result["model"] == "mock-model"
        assert result["tokens"] == 100
        assert result["output"] == "Mock output"

def test_benchmark_server_error():
    """Test the benchmark function with a mocked server error."""
    mock_response = MagicMock()
    mock_response.status_code = 500
    mock_response.text = "Internal Server Error"

    with patch("requests.post", return_value=mock_response):
        result = benchmark("Test prompt", "http://mockserver.com", 256)
        assert result is None

def test_benchmark_invalid_url():
    """Test the benchmark function with an invalid server URL."""
    with pytest.raises(Exception):
        benchmark("Test prompt", "invalid_url", 256)

def test_cli_argument_parsing():
    """Test CLI argument parsing."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", type=str)
    parser.add_argument("--promptfile", type=str)
    parser.add_argument("--server_url", type=str, default="http://localhost:1234/v1/chat/completions")
    parser.add_argument("--max_tokens", type=int, default=512)

    args = parser.parse_args(["--prompt", "Test prompt", "--max_tokens", "256"])
    assert args.prompt == "Test prompt"
    assert args.max_tokens == 256
    assert args.server_url == "http://localhost:1234/v1/chat/completions"

def test_main_no_arguments(capsys):
    """Test the main function with no arguments."""
    with patch("argparse.ArgumentParser.parse_args", return_value=argparse.Namespace(prompt=None, promptfile=None, server_url=None, max_tokens=512)):
        main()
        captured = capsys.readouterr()
        assert "Error: Please provide --prompt or --promptfile." in captured.out
