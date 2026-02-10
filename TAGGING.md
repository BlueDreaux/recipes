# Recipe Tagging System

This repository uses a multi-tag categorization system to organize recipes by various attributes. Each recipe can have multiple tags across different categories.

## Tag Categories

### 1. Ingredients
Tags that identify the main or key ingredients in a recipe.

Examples: `chicken`, `beef`, `pasta`, `tomato`, `chocolate`, `cheese`, `eggs`, `fish`, `vegetarian`, `vegan`

### 2. Type of Dish
Tags that identify what kind of dish this is.

Examples: `appetizer`, `main-course`, `side-dish`, `dessert`, `soup`, `salad`, `breakfast`, `lunch`, `dinner`, `snack`, `beverage`

### 3. Occasions
Tags that identify when or for what event this dish is appropriate.

Examples: `holiday`, `thanksgiving`, `christmas`, `birthday`, `party`, `picnic`, `bbq`, `weeknight`, `weekend`, `special-occasion`, `everyday`

### 4. Additional Categories
You can also use other categories as needed:
- **Cuisine**: `italian`, `mexican`, `chinese`, `indian`, `french`, `american`
- **Cooking Method**: `baked`, `grilled`, `fried`, `slow-cooker`, `instant-pot`, `no-cook`
- **Dietary**: `gluten-free`, `dairy-free`, `low-carb`, `keto`, `paleo`
- **Difficulty**: `easy`, `moderate`, `advanced`
- **Time**: `quick` (under 30 min), `medium` (30-60 min), `long` (over 60 min)

## How to Tag Recipes

Add tags to your recipe markdown files using YAML frontmatter at the top of the file:

```yaml
---
title: "Recipe Name"
tags:
  ingredients:
    - chicken
    - garlic
    - lemon
  type:
    - main-course
    - dinner
  occasion:
    - weeknight
    - special-occasion
  cuisine:
    - italian
  method:
    - baked
  dietary:
    - gluten-free
  difficulty: easy
  time: medium
---
```

Alternatively, you can use a simpler flat tag structure:

```yaml
---
title: "Recipe Name"
tags:
  - chicken
  - main-course
  - weeknight
  - italian
  - baked
  - gluten-free
  - easy
---
```

## Browsing by Tags

Use the tag index files in the `tags/` directory to find recipes by specific tags. Each tag category has its own subdirectory with markdown files listing recipes that match each tag.

You can also use standard file search tools:
```bash
# Find all recipes tagged with "chicken"
grep -r "chicken" --include="*.md" recipes/

# Find recipes with multiple tags
grep -l "chicken" recipes/*.md | xargs grep -l "italian"
```

## Tag Naming Conventions

- Use lowercase for all tags
- Use hyphens (-) for multi-word tags (e.g., `slow-cooker`, `main-course`)
- Keep tags concise and descriptive
- Use consistent tag names across recipes (e.g., always use `chicken`, not sometimes `chicken` and sometimes `poultry`)

## Contributing

When adding a new recipe:
1. Add appropriate tags in the frontmatter
2. Update the relevant tag index files if they exist
3. Consider whether your recipe introduces any new useful tags
