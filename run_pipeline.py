from obsidian_to_hugo import ObsidianToHugo

obsidian_to_hugo = ObsidianToHugo(
    obsidian_vault_dir="hugo vault",
    hugo_content_dir="content",
)

obsidian_to_hugo.run()