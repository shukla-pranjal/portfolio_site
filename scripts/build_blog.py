import os
import markdown
from datetime import datetime

# Define directories
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POSTS_DIR = os.path.join(BASE_DIR, 'posts')
BLOG_DIR = os.path.join(BASE_DIR, 'blog')
TEMPLATE_INDEX = os.path.join(BASE_DIR, 'blog.html')

# Ensure blog output dir exists
os.makedirs(BLOG_DIR, exist_ok=True)

# Basic HTML template for individual posts
POST_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Pranjal Kumar Shukla</title>
    <!-- Using Plus Jakarta Sans for that premium modern tech feel -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../styles/main.css">
</head>
<body>
    <div class="glow-orb orb-1"></div>

    <nav class="glass-nav">
        <div class="nav-content">
            <a href="../index.html" class="logo">P.</a>
            <div class="links">
                <a href="../index.html#experience">Experience</a>
                <a href="../index.html#projects">Work</a>
                <a href="../blog.html" class="active">Blog</a>
            </div>
            <a href="mailto:pranjalmss2005@gmail.com" class="btn btn-nav">Contact</a>
        </div>
    </nav>

    <main class="section">
        <article class="post-header" style="padding-top: 6rem;">
            <div class="blog-date">{date}</div>
            <h1>{title}</h1>
        </article>
        <div class="post-content">
            {content}
        </div>
    </main>

    <footer>
        <p>&copy; 2026 Pranjal Kumar Shukla.</p>
    </footer>
</body>
</html>
"""

def build_blog():
    print("Building blog...")
    if not os.path.exists(POSTS_DIR):
        print(f"Directory {POSTS_DIR} does not exist. Please create it and add markdown files.")
        return

    post_list_html = ""
    
    # Get all markdown files and sort by modification time (or parse frontmatter if preferred)
    # Here we just sort alphabetically or by creation time
    md_files = [f for f in os.listdir(POSTS_DIR) if f.endswith('.md')]
    
    posts_data = []
    
    for filename in md_files:
        filepath = os.path.join(POSTS_DIR, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        # Very simple frontmatter extraction (first line # Title)
        title = filename.replace('.md', '').replace('-', ' ').title()
        if lines and lines[0].startswith('# '):
            title = lines[0].replace('# ', '').strip()
            # remove the title from the content so it's not duplicated
            lines = lines[1:]
            
        content_md = ''.join(lines)
        
        # Convert markdown to HTML
        html_content = markdown.markdown(content_md, extensions=['fenced_code', 'tables'])
        
        # Determine output filename
        output_filename = filename.replace('.md', '.html')
        output_path = os.path.join(BLOG_DIR, output_filename)
        
        # Get date
        mod_time = os.path.getmtime(filepath)
        date_str = datetime.fromtimestamp(mod_time).strftime('%B %d, %Y')
        
        # Write post HTML
        post_html = POST_TEMPLATE.format(
            title=title,
            date=date_str,
            content=html_content
        )
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(post_html)
            
        posts_data.append({
            'title': title,
            'date': date_str,
            'url': f"blog/{output_filename}",
            'mod_time': mod_time
        })
        print(f"Generated {output_filename}")
        
    # Sort posts by newest
    posts_data.sort(key=lambda x: x['mod_time'], reverse=True)
    
    # Generate blog index list
    for post in posts_data:
        post_list_html += f"""
        <div class="blog-post-card">
            <div class="blog-date">{post['date']}</div>
            <h2><a href="{post['url']}">{post['title']}</a></h2>
        </div>
        """
        
    # Update blog.html
    with open(TEMPLATE_INDEX, 'r', encoding='utf-8') as f:
        blog_index_content = f.read()
        
    # Replace placeholder
    updated_index = blog_index_content.replace('<!-- REPLACE_ME_WITH_POSTS -->', post_list_html)
    
    # Save the updated blog.html (We write it to the same file or a built version. 
    # To keep it simple, we'll overwrite blog.html, but normally we'd write to a 'dist' folder)
    with open(TEMPLATE_INDEX, 'w', encoding='utf-8') as f:
        f.write(updated_index)
        
    print("Blog build complete!")

if __name__ == "__main__":
    build_blog()
