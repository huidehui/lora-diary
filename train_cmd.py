import subprocess

# 设定命令行参数
command = [
    "accelerate", "launch", "--num_cpu_threads_per_process", "1", "train_network.py",
    "--pretrained_model_name_or_path", "D:\Probject\model\v1-5-pruned.safetensors",
    "--dataset_config", "data-config/kobi.toml",
    "--output_dir", "out",
    "--output_name", "kobi_model",
    "--save_model_as", "safetensors",
    "--prior_loss_weight", "1.0",
    "--max_train_steps", "400",
    "--learning_rate", "1e-4",
    "--optimizer_type", "AdamW8bit",
    "--xformers",
    "--mixed_precision", "fp16",
    "--cache_latents",
    "--gradient_checkpointing",
    "--save_every_n_epochs", "1",
    "--network_module", "networks.lora"
]

# 执行命令
try:
    result = subprocess.run(command, check=True, text=True, capture_output=True,shell=True)
    print("命令执行成功：", result.stdout)
except subprocess.CalledProcessError as e:
    print("命令执行失败：", e.stderr)

accelerate launch --num_cpu_threads_per_process 1 train_network.py
    --pretrained_model_name_or_path="D:\Probject\model\v1-5-pruned.safetensors"
    --dataset_config="data-config/kobi.toml"
    --output_dir="out"
    --output_name="kobi-model"
    --save_model_as=safetensors
    --prior_loss_weight=1.0
    --max_train_steps=400
    --learning_rate=1e-4
    --optimizer_type="AdamW8bit"
    --xformers
    --mixed_precision="fp16"
    --cache_latents
    --gradient_checkpointing
    --save_every_n_epochs=1
    --network_module=networks.lora