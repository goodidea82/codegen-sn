# CUDA_VISIBLE_DEVICES=0 pm2 start --name "llm1" "vllm serve thesven/Mistral-7B-Instruct-v0.3-GPTQ  --max-model-len 8192 --dtype half --gpu-memory-utilization 0.3 --api-key 40aba48bca99c74312081ec209dddeb7 --port 16386"

# CUDA_VISIBLE_DEVICES=0 pm2 start --name "code1" "vllm serve Qwen/CodeQwen1.5-7B-AWQ --max-model-len 65536 --dtype half --gpu-memory-utilization 0.65 --api-key 40aba48bca99c74312081ec209dddeb7 --port 16414"


# CUDA_VISIBLE_DEVICES=1 pm2 start --name "llm2" "vllm serve thesven/Mistral-7B-Instruct-v0.3-GPTQ  --max-model-len 8192 --gpu-memory-utilization 0.2 --api-key 40aba48bca99c74312081ec209dddeb7 --port 16457 --quantization gptq" #--dtype half 

CUDA_VISIBLE_DEVICES=0,1 pm2 start --name "code2" "vllm serve deepseek-ai/DeepSeek-Coder-V2-Base --dtype auto --max-model-len 8192 --gpu-memory-utilization 0.95 --api-key 40aba48bca99c74312081ec209dddeb7 --port 16571 --trust-remote-code --tensor-parallel-size 2 --num-shards 2" #--dtype half 



# pm2 start --name "qwen" "vllm serve Qwen/CodeQwen1.5-7B  --max-model-len 8192 --dtype half --gpu-memory-utilization 0.3 --port 16702"