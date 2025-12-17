"""
Automated MDX Template Generator for Bilingual Documentation

This script helps convert existing .md files to bilingual .mdx format.

Usage:
    python generate_mdx_template.py <input_md_file> <output_mdx_file> <page_function_name>

Example:
    python generate_mdx_template.py docs/module1/ros2-fundamentals.md docs/module1/ros2-fundamentals.mdx ROS2Fundamentals
"""

import sys
import re

def generate_mdx_template(input_file, output_file, function_name):
    """Generate bilingual MDX template from markdown file"""
    
    # Read the original markdown
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract frontmatter
    frontmatter_match = re.match(r'^---\r?\n(.*?)\r?\n---\r?\n', content, re.DOTALL)
    if frontmatter_match:
        frontmatter = frontmatter_match.group(1)
        markdown_content = content[frontmatter_match.end():]
    else:
        frontmatter = "sidebar_position: 1"
        markdown_content = content
    
    # Convert markdown to JSX (basic conversion)
    def md_to_jsx(text):
        """Convert markdown to JSX format"""
        lines = []
        in_code_block = False
        in_list = False
        
        for line in text.split('\n'):
            line = line.rstrip()
            
            # Code blocks
            if line.startswith('```'):
                if in_code_block:
                    lines.append('</pre>')
                    in_code_block = False
                else:
                    lines.append('<pre>')
                    in_code_block = True
                continue
            
            if in_code_block:
                lines.append(line)
                continue
            
            # Headers
            if line.startswith('# '):
                lines.append(f'<h1>{line[2:]}</h1>')
            elif line.startswith('## '):
                lines.append(f'<h2>{line[3:]}</h2>')
            elif line.startswith('### '):
                lines.append(f'<h3>{line[4:]}</h3>')
            elif line.startswith('#### '):
                lines.append(f'<h4>{line[5:]}</h4>')
            
            # Lists
            elif line.startswith('- ') or line.startswith('* '):
                if not in_list:
                    lines.append('<ul>')
                    in_list = True
                lines.append(f'<li>{line[2:]}</li>')
            elif line.startswith('1. ') or re.match(r'^\d+\. ', line):
                if not in_list:
                    lines.append('<ol>')
                    in_list = True
                content = re.sub(r'^\d+\. ', '', line)
                lines.append(f'<li>{content}</li>')
            else:
                if in_list:
                    if  line.startswith('  '):
                        # Nested list item
                        lines.append(f'  <li>{line.strip()}</li>')
                    else:
                        # End of list
                        lines.append('</ul>' if lines[-1].endswith('</li>') else '</ol>')
                        in_list = False
                        if line.strip():
                            lines.append(f'<p>{line}</p>')
                elif line.strip():
                    # Regular paragraph
                    lines.append(f'<p>{line}</p>')
                elif lines:  # Empty line
                    lines.append('')
        
        # Close any open lists
        if in_list:
            lines.append('</ul>')
        
        return '\n'.join(lines)
    
    english_jsx = md_to_jsx(markdown_content)
    
    # Generate the MDX template
    mdx_content = f"""---
{frontmatter}
---

import {{useTranslation}} from 'react-i18next';

export default function {function_name}() {{
  const {{i18n}} = useTranslation();
  const isUrdu = i18n.language === 'ur';
  
  if (isUrdu) {{
    return (
      <div>
        {{/* 
        ⚠️ URDU TRANSLATION NEEDED ⚠️
        
        Instructions:
        1. Translate the English content below to Urdu
        2. Keep all HTML tags exactly as they are
        3. Keep code blocks, technical terms in English where appropriate
        4. Translate headings, paragraphs, list items
        5. Maintain proper Urdu grammar and terminology
        
        Use Google Translate or ChatGPT for translation, then review for accuracy.
        */}}
        
        <h1>اردو ترجمہ یہاں درج کریں</h1>
        <p>براہ کرم نیچے دیے گئے انگریزی مواد کا ترجمہ کریں۔</p>
        
        {{/* TODO: Replace content below with Urdu translation */}}
      </div>
    );
  }}
  
  return (
    <div>
{english_jsx}
    </div>
  );
}}
"""
    
    # Write the output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(mdx_content)
    
    print(f"✅ Template created: {output_file}")
    print(f"📝 Next steps:")
    print(f"   1. Translate the Urdu section in the file")
    print(f"   2. Delete the original .md file: {input_file}")
    print(f"   3. Test the page by switching to Urdu")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python generate_mdx_template.py <input_md> <output_mdx> <FunctionName>")
        print("\nExample:")
        print("  python generate_mdx_template.py docs/module1/ros2-fundamentals.md docs/module1/ros2-fundamentals.mdx ROS2Fundamentals")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    function_name = sys.argv[3]
    
    generate_mdx_template(input_file, output_file, function_name)
