---
name: ui-ux-pro-max-skill
description: AI-powered design intelligence toolkit providing searchable databases of UI styles, color palettes, font pairings, chart types, and UX guidelines.
---

# UI/UX Pro Max

AI-powered design intelligence toolkit providing searchable databases of UI styles, color palettes, font pairings, chart types, and UX guidelines.

## Use this skill when

- Designing professional UI/UX for multiple platforms
- Searching for UI styles (glassmorphism, minimalism, brutalism)
- Selecting font pairings and color palettes
- Planning page structures and CTA strategies
- Implementing charts and data visualizations
- Following UX best practices and avoiding anti-patterns

## Instructions

### Search for Design Intelligence
Use the following command to search for specific design patterns or tokens:
```bash
python3 src/ui-ux-pro-max/scripts/search.py "<query>" --domain <domain> [-n <max_results>]
```

**Domains:**
- `product`: SaaS, e-commerce, portfolio
- `style`: glassmorphism, minimalism, brutalism
- `typography`: font pairings
- `color`: palettes by product type
- `landing`: page structure and CTA
- `chart`: chart types and libraries
- `ux`: best practices

### Generation
The skill can also assist in generating design systems and consistent UI patterns across different stacks: `react`, `nextjs`, `shadcn`, `tailwind`, `flutter`, `swiftui`, etc.

## Resources
- `src/ui-ux-pro-max/data/`: Searchable CSV databases.
- `src/ui-ux-pro-max/scripts/`: Search and generation engine.
