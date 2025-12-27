
import os

def fix_html_paths(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".html") or filename.endswith(".rss"):
                file_path = os.path.join(dirpath, filename)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                content = content.replace("https://mintylime.co.ke/wp-content/", "/assets/")
                content = content.replace("http://mintylime.co.ke/wp-content/", "/assets/")
                content = content.replace("wp-content/uploads/elementor/google-fonts/css/", "assets/css/")

                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)

fix_html_paths("src")
