from obsidian_to_hugo import ObsidianToHugo

obsidian_to_hugo = ObsidianToHugo(
    obsidian_vault_dir="./wiki/",
    hugo_content_dir="./content/wow/",
)

obsidian_to_hugo.run()
