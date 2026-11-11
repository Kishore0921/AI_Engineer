from huggingface_hub import HfApi


def explore_models(task="text-classification", limit=3):
    api = HfApi()
    print(f"Searching Hugging Face Hub for top '{task}' models...\n")

    # Fetch top models sorted by download count
    models = api.list_models(
        task=task, sort="downloads", direction=-1, limit=limit
    )

    model_list = list(models)
    if not model_list:
        print("No models found for this task.")
        return

    print("=" * 65)
    print(f"MODEL EXPLORATION REPORT (Task: {task})")
    print("=" * 65)

    for idx, model in enumerate(model_list, start=1):
        # Fetch detailed model info (similar to viewing the model card metadata)
        info = api.model_info(model.id)

        print(f"\n[{idx}] Model ID: {info.id}")
        print(f"    Task:         {info.pipeline_tag}")
        print(f"    Downloads:    {info.downloads:,}")
        print(f"    Likes:        {info.likes:,}")
        print(f"    Library:      {info.library_name or 'Not specified'}")
        print(f"    Last Updated: {info.last_modified.strftime('%Y-%m-%d')}")

        # Display up to 5 tags from the model card
        tags = (
            ", ".join(info.tags[:5])
            if info.tags
            else "No tags available"
        )
        print(f"    Key Tags:     {tags}")
        print("-" * 65)


if __name__ == "__main__":
    # You can change the task to 'text-generation', 'summarization', 'translation', etc.
    user_task = (
        input(
            "Enter a task to search (press Enter for 'text-classification'): "
        ).strip()
        or "text-classification"
    )
    explore_models(task=user_task, limit=3)
