# bench.py
import time
import requests
import argparse

# LM_STUDIO_URL = "http://localhost:1234/v1/chat/completions"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": "Bearer lm-studio"
}

def benchmark(prompt, server_url, max_tokens):
    payload = {
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": max_tokens
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer lm-studio"
    }
    start_time = time.time()
    response = requests.post(server_url, headers=headers, json=payload)
    end_time = time.time()

    if response.status_code != 200:
        print(f"Error: {response.status_code} {response.text}")
        return None

    elapsed = end_time - start_time
    data = response.json()

    tokens = data.get('usage', {}).get('total_tokens', 0)
    tokens_per_sec = tokens / elapsed if elapsed > 0 else 0
    model_name = data.get('model', 'Unknown')
    output_content = data.get('choices', [{}])[0].get('message', {}).get('content', '').strip()

    return {
        "prompt": prompt,
        "latency": elapsed,
        "tokens": tokens,
        "tokens_per_sec": tokens_per_sec,
        "model": model_name,
        "output": output_content
    }

def main():
    parser = argparse.ArgumentParser(description="Benchmark LLM via LM Studio server")
    parser.add_argument("--prompt", type=str, help="Prompt to test")
    parser.add_argument("--promptfile", type=str, help="File containing prompts")
    parser.add_argument("--model", type=str, required=False, help="(Optional) Model name")
    parser.add_argument("--max_tokens", type=int, default=512, help="Maximum tokens to generate")
    parser.add_argument(
    "--server_url",
    type=str,
    default="http://localhost:1234/v1/chat/completions",
    help="LM Studio server URL (default: http://localhost:1234/v1/chat/completions)"
)
    args = parser.parse_args()

    prompts = []

    if args.prompt:
        prompts.append(args.prompt)
    elif args.promptfile:
        with open(args.promptfile, "r", encoding="utf-8") as f:
            prompts = [line.strip() for line in f if line.strip()]
    else:
        print("Error: Please provide --prompt or --promptfile.")
        return

    results = []
    for prompt in prompts:
        print(f"Testing prompt: {prompt}")
        result = benchmark(prompt, args.server_url, args.max_tokens)
        if result:
            results.append(result)
            print(f"Model: {result['model']}, Latency: {result['latency']:.2f} sec, Tokens: {result['tokens']}, Tokens/sec: {result['tokens_per_sec']:.2f}")
            print(f"Output: {result['output']}")
            print("-" * 40)

    if len(results) > 1:
        avg_latency = sum(r['latency'] for r in results) / len(results)
        avg_tokens_sec = sum(r['tokens_per_sec'] for r in results) / len(results)
        print(f"\nAverage Latency: {avg_latency:.2f} sec, Average Tokens/sec: {avg_tokens_sec:.2f}")

if __name__ == "__main__":
    main()


