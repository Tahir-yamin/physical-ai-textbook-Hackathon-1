# GitHub Pages Deployment Guide

## Prerequisites
- GitHub account
- Repository with Docusaurus project
- Node.js installed locally

## Deployment Steps

### 1. Configure Docusaurus for GitHub Pages

Edit `docusaurus.config.ts`:
```typescript
const config: Config = {
  url: 'https://YOUR_USERNAME.github.io',
  baseUrl: '/physical-ai-textbook/',
  organizationName: 'YOUR_USERNAME',
  projectName: 'physical-ai-textbook',
  deploymentBranch: 'gh-pages',
  trailingSlash: false,
};
```

### 2. Add Deployment Script

In `package.json`, ensure you have:
```json
{
  "scripts": {
    "deploy": "docusaurus deploy"
  }
}
```

### 3. Build and Deploy

```bash
cd textbook
npm run build
npm run deploy
```

This will:
- Build the static site
- Create/update the `gh-pages` branch
- Push to GitHub

### 4. Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings**
3. Navigate to **Pages** (left sidebar)
4. Under **Source**, select:
   - Branch: `gh-pages`
   - Folder: `/ (root)`
5. Click **Save**

### 5. Verify Deployment

Your site will be available at:
```
https://YOUR_USERNAME.github.io/physical-ai-textbook/
```

It may take a few minutes for the first deployment.

## Custom Domain (Optional)

### Add Custom Domain

1. In repository **Settings** → **Pages**
2. Enter your custom domain (e.g., `textbook.example.com`)
3. Click **Save**

### Configure DNS

Add a CNAME record in your DNS provider:
```
CNAME textbook YOUR_USERNAME.github.io
```

### Update Docusaurus Config

```typescript
const config: Config = {
  url: 'https://textbook.example.com',
  baseUrl: '/',
};
```

## Automated Deployment with GitHub Actions

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: 20
          
      - name: Install dependencies
        run: |
          cd textbook
          npm ci
          
      - name: Build
        run: |
          cd textbook
          npm run build
          
      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./textbook/build
```

This will automatically deploy on every push to `main`.

## Troubleshooting

### 404 Errors
- Check `baseUrl` in `docusaurus.config.ts`
- Verify GitHub Pages is enabled
- Check the `gh-pages` branch exists

### Build Failures
```bash
# Clear cache and rebuild
npm run clear
npm run build
```

### Assets Not Loading
- Ensure `baseUrl` matches your repository name
- Check for absolute paths in code (should be relative)

## Backend Deployment

The backend (FastAPI) needs separate hosting:

### Options:
1. **Render.com** (Free tier available)
2. **Railway.app** (Free tier available)
3. **Fly.io** (Free tier available)
4. **Heroku** (Paid)

### Environment Variables
Ensure these are set in your hosting platform:
- `OPENROUTER_API_KEY`
- `QDRANT_URL`
- `QDRANT_API_KEY`
- `DATABASE_URL` (Neon PostgreSQL)

### CORS Configuration
Update `main.py` to allow your GitHub Pages domain:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://YOUR_USERNAME.github.io",
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Monitoring

- **GitHub Actions**: Check deployment status
- **GitHub Pages**: View deployment history in Settings
- **Analytics**: Add Google Analytics or similar

## Maintenance

### Update Content
1. Make changes locally
2. Test with `npm start`
3. Commit and push to `main`
4. GitHub Actions will auto-deploy (if configured)

Or manually:
```bash
npm run deploy
```

### Rollback
```bash
git checkout gh-pages
git reset --hard <previous-commit-hash>
git push -f origin gh-pages
```

---

**Need help?** Check [Docusaurus Deployment Docs](https://docusaurus.io/docs/deployment)
