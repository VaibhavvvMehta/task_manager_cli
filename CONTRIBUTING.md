# Contributing to Task Manager CLI

Thanks for contributing! Here's what you need to know:

## Branching

We use a simple Git Flow model with two permanent branches:

- **`main`** - Contains stable, production-ready code. Only gets updated from `develop` or hotfixes
- **`develop`** - Integration branch where all new features come together. This is our "latest development" branch

### How It Works

```
main     ──●────────●──────── (releases)
            \      /
develop  ────●──●──●──●───── (continuous development)
              \    /
feature   ────●──●─── (your work)
```

### Branch Types & Workflow

#### Feature Branches
**When**: Adding new functionality or making any changes
**Branch from**: `develop`  
**Merge back to**: `develop`

**Branch naming:**
- `feature/short-description` - for new features
- `fix/short-description` - for bug fixes
- `docs/short-description` - for documentation updates

```bash
# Start working on something new
git checkout develop
git pull origin develop
git checkout -b feature/add-task-priority

# Work on your changes...
git add .
git commit -m "feat: add priority field to tasks"

# Push and create PR to develop
git push origin feature/add-task-priority
```

### Complete Workflow Example

1. **Create your branch** from `develop`
2. **Make your changes** and commit them
3. **Push your branch** to GitHub
4. **Open a Pull Request** to merge into `develop`
5. **After review**, your PR gets merged to `develop`
6. **Periodically**, `develop` gets merged to `main` for releases

## Pull Requests

Pull Requests (PRs) are how your code gets into the main project. Here's the complete process:

### 1. Before Creating a PR

**Test your changes:**
```bash
# Run all tests
python -m pytest test/

# Test your specific changes manually
python task_manager.py  # make sure it works
```

**Make sure your branch is up to date:**
```bash
git checkout develop
git pull origin develop
git checkout your-branch-name
git merge develop  # or git rebase develop
```

### 2. Creating the PR

**PR Titles** - Use these prefixes:
- `feat:` for new features ("feat: add task priority sorting")
- `fix:` for bug fixes ("fix: resolve date parsing error")
- `docs:` for documentation ("docs: update installation guide")
- `test:` for adding tests ("test: add unit tests for task deletion")

**PR Description** - Use this template:
```
## What changed?
Clear description of what you added/fixed/changed.

## Why?
Why was this change needed?

## How to test?
1. Step-by-step instructions
2. What should happen
3. Any edge cases to check

## Checklist
- [ ] Tests pass locally
- [ ] Code follows project style
- [ ] Tested the changes manually
- [ ] Updated docs if needed
```

### 3. PR Review Process

1. **Automated checks** - GitHub will run tests automatically
2. **Code review** - A maintainer will review your code
3. **Feedback** - You might need to make changes based on feedback
4. **Approval** - Once approved, your PR gets merged to `develop`

### 4. After Your PR is Merged

Clean up your local branches:
```bash
git checkout develop
git pull origin develop  # get the latest changes
git branch -d your-branch-name  # delete your local branch
```

## Code Style

- Follow Python conventions (PEP 8)
- Write clear function names
- Add comments for complex logic
- Keep functions short and focused

## Testing

Run tests before submitting:
```bash
python -m pytest test/
```

Write tests for new features in the `test/` directory.

---

That's it! Keep it simple.Thank YOU !!