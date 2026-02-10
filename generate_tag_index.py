#!/usr/bin/env python3
"""
Recipe Tag Indexer

This script scans all recipe markdown files and generates index files
organized by tags. It parses YAML frontmatter to extract tags and creates
browsable indexes in the tags/ directory.
"""

import os
import re
import yaml
from pathlib import Path
from collections import defaultdict


def parse_frontmatter(content):
    """Extract YAML frontmatter from markdown content."""
    pattern = r'^---\s*\n(.*?)\n---\s*\n'
    match = re.match(pattern, content, re.DOTALL)
    if match:
        try:
            return yaml.safe_load(match.group(1))
        except yaml.YAMLError as e:
            print(f"Error parsing YAML: {e}")
            return None
    return None


def extract_tags(frontmatter):
    """Extract all tags from frontmatter in a structured way."""
    if not frontmatter or 'tags' not in frontmatter:
        return {}
    
    tags = frontmatter['tags']
    
    # Handle both structured and flat tag formats
    if isinstance(tags, dict):
        # Structured format with categories
        result = {}
        for category, values in tags.items():
            if isinstance(values, list):
                result[category] = values
            else:
                # Single value (like difficulty: easy)
                result[category] = [values]
        return result
    elif isinstance(tags, list):
        # Flat list format - categorize as 'general'
        return {'general': tags}
    
    return {}


def scan_recipes(recipes_dir):
    """Scan all recipe files and extract their metadata."""
    recipes_data = []
    
    for recipe_file in Path(recipes_dir).glob('*.md'):
        with open(recipe_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        frontmatter = parse_frontmatter(content)
        if frontmatter:
            tags = extract_tags(frontmatter)
            title = frontmatter.get('title', recipe_file.stem)
            
            recipes_data.append({
                'filename': recipe_file.name,
                'title': title,
                'tags': tags,
                'path': str(recipe_file.relative_to(recipes_dir.parent))
            })
    
    return recipes_data


def build_tag_indexes(recipes_data):
    """Build indexes organized by tag categories and values."""
    indexes = defaultdict(lambda: defaultdict(list))
    
    for recipe in recipes_data:
        for category, tags in recipe['tags'].items():
            for tag in tags:
                indexes[category][tag].append({
                    'title': recipe['title'],
                    'path': recipe['path']
                })
    
    return indexes


def write_tag_index(tags_dir, category, tag, recipes):
    """Write an index file for a specific tag."""
    category_dir = Path(tags_dir) / category
    category_dir.mkdir(parents=True, exist_ok=True)
    
    index_file = category_dir / f"{tag}.md"
    
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(f"# Recipes tagged with: {tag}\n\n")
        f.write(f"**Category:** {category}\n\n")
        f.write(f"Found {len(recipes)} recipe(s):\n\n")
        
        for recipe in sorted(recipes, key=lambda x: x['title']):
            # Create relative link from tags/category/ to recipes/
            f.write(f"- [{recipe['title']}](../../{recipe['path']})\n")


def write_category_index(tags_dir, category, tags):
    """Write an index file listing all tags in a category."""
    category_dir = Path(tags_dir) / category
    category_dir.mkdir(parents=True, exist_ok=True)
    
    index_file = category_dir / "README.md"
    
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(f"# {category.title()} Tags\n\n")
        f.write(f"Browse recipes by {category}:\n\n")
        
        for tag in sorted(tags.keys()):
            count = len(tags[tag])
            f.write(f"- [{tag}]({tag}.md) ({count} recipe{'s' if count != 1 else ''})\n")


def write_main_index(tags_dir, indexes):
    """Write the main tags index file."""
    index_file = Path(tags_dir) / "README.md"
    
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write("# Recipe Tags Index\n\n")
        f.write("Browse recipes by category:\n\n")
        
        for category in sorted(indexes.keys()):
            tag_count = len(indexes[category])
            recipe_count = sum(len(recipes) for recipes in indexes[category].values())
            f.write(f"## [{category.title()}]({category}/README.md)\n\n")
            f.write(f"{tag_count} tag{'s' if tag_count != 1 else ''}, ")
            f.write(f"{recipe_count} recipe{'s' if recipe_count != 1 else ''}\n\n")


def main():
    """Main function to generate all tag indexes."""
    # Get the repository root directory
    script_dir = Path(__file__).parent
    recipes_dir = script_dir / "recipes"
    tags_dir = script_dir / "tags"
    
    if not recipes_dir.exists():
        print(f"Recipes directory not found: {recipes_dir}")
        return
    
    print("Scanning recipes...")
    recipes_data = scan_recipes(recipes_dir)
    print(f"Found {len(recipes_data)} recipes")
    
    print("Building tag indexes...")
    indexes = build_tag_indexes(recipes_data)
    
    print("Writing index files...")
    for category, tags in indexes.items():
        for tag, recipes in tags.items():
            write_tag_index(tags_dir, category, tag, recipes)
        write_category_index(tags_dir, category, tags)
    
    write_main_index(tags_dir, indexes)
    
    print("Done! Tag indexes generated in tags/ directory")


if __name__ == "__main__":
    main()
