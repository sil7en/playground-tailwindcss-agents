# Agents Instructions

This project has specific guidelines that must be followed by any agent working on it.

## Styling Guidelines
- **Tailwind CSS Only**: This project relies exclusively on Tailwind CSS for styling. Do not write custom CSS in separate files unless absolutely necessary for things Tailwind cannot handle (which is rare).
- **Neobrutalist Design**: The visual style of this project is **Neobrutalism**.
  - Use bold, high-contrast colors.
  - Use thick black borders (e.g., `border-2` or `border-4` with `border-black`).
  - Use hard, non-blurred shadows (e.g., `box-shadow: 4px 4px 0px 0px #000`).
  - Typography should be distinct and readable, fitting a youthful and educational theme.

## Workflow
- **Build Process**: After completing any task that involves code changes, you **MUST** run the following command to ensure styles are correctly compiled:
  ```bash
  npm run build:css
  ```
