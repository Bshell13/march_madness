import kagglehub

def main():
  # Download latest version
  path = kagglehub.dataset_download("jonathanpilafas/2024-march-madness-statistical-analysis")

  print("Path to dataset files:", path)

if __name__ == "__main__":
  main()
