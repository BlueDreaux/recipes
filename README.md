# Recipes Collection

A shareable collection of recipes organized with a flexible multi-tag categorization system.

## Features

✨ **Multi-Tag Categorization**: Organize recipes by multiple attributes including:
- 🥘 **Ingredients**: Main and key ingredients (chicken, tomato, chocolate, etc.)
- 🍽️ **Type of Dish**: Appetizers, main courses, desserts, salads, etc.
- 🎉 **Occasions**: Weeknight dinners, holidays, parties, BBQs, etc.
- 🌍 **Cuisine**: Italian, Greek, American, Mexican, etc.
- 👨‍🍳 **Cooking Method**: Baked, grilled, no-cook, slow-cooker, etc.
- 🥗 **Dietary**: Vegetarian, vegan, gluten-free, dairy-free, etc.

📑 **Automatic Tag Indexes**: Browse recipes by any tag category using auto-generated indexes

## Quick Start

### Browse Recipes

1. **Browse all recipes**: Check the [`recipes/`](recipes/) directory
2. **Browse by tags**: Check the [`tags/`](tags/) directory for organized indexes
3. **Read the tagging guide**: See [`TAGGING.md`](TAGGING.md) for detailed information

### Add a New Recipe

1. Create a new markdown file in the `recipes/` directory
2. Add YAML frontmatter with tags (see example below)
3. Write your recipe content
4. Run `python3 generate_tag_index.py` to update the tag indexes

#### Example Recipe Template

```markdown
---
title: "Your Recipe Name"
tags:
  ingredients:
    - main-ingredient
    - key-ingredient
  type:
    - main-course
    - dinner
  occasion:
    - weeknight
  cuisine:
    - italian
  method:
    - baked
  difficulty: easy
  time: quick
---

# Your Recipe Name
Description of your recipe.

## Notes
Any additional tips or variations

## Ingredients
- List your ingredients here

## Instructions
1. Step by step instructions
2. Continue...

```

## Repository Structure

```
recipes/
├── README.md                      # This file
├── TAGGING.md                     # Detailed tagging system documentation
├── generate_tag_index.py          # Script to generate tag indexes
├── recipes/                       # All recipe markdown files
│   ├── chicken-parmesan.md
│   ├── chocolate-chip-cookies.md
│   └── greek-salad.md
└── tags/                          # Auto-generated tag indexes
    ├── README.md                  # Main tag index
    ├── ingredients/               # Recipes by ingredient
    ├── type/                      # Recipes by dish type
    ├── occasion/                  # Recipes by occasion
    ├── cuisine/                   # Recipes by cuisine
    ├── method/                    # Recipes by cooking method
    └── dietary/                   # Recipes by dietary restrictions
```

## Tools

### Generate Tag Indexes

After adding or modifying recipes, regenerate the tag indexes:

```bash
python3 generate_tag_index.py
```

This will scan all recipe files and update the browsable tag indexes in the `tags/` directory.

### Search for Recipes

Use grep to search for specific tags or ingredients:

```bash
# Find all recipes with "chicken"
grep -r "chicken" --include="*.md" recipes/

# Find recipes that are both "vegetarian" and "quick"
grep -l "vegetarian" recipes/*.md | xargs grep -l "quick"
```

## Contributing

Contributions are welcome! When adding recipes:

1. Follow the tagging conventions in [`TAGGING.md`](TAGGING.md)
2. Use consistent tag names
3. Regenerate tag indexes with `python3 generate_tag_index.py`
4. Ensure your recipe includes clear instructions and ingredient lists

## Example Recipes

Check out these example recipes to see the tagging system in action:

- [Chicken Parmesan](recipes/chicken-parmesan.md) - Italian main course
- [Chocolate Chip Cookies](recipes/chocolate-chip-cookies.md) - Classic dessert
- [Greek Salad](recipes/greek-salad.md) - Quick and healthy side dish

## License

Feel free to use and share these recipes!
