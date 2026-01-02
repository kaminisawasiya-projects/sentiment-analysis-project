# Render Deployment Guide

## ✅ All Issues Fixed!

### Problems Identified & Resolved:

1. **Missing Procfile** ✅ FIXED
   - Created `Procfile` with: `web: gunicorn app:app`

2. **Large CSV File (66MB)** ✅ FIXED
   - Modified `app.py` to handle missing CSV gracefully
   - App will use dummy data if `reviews.csv` is not found
   - You can exclude the CSV from deployment

3. **Debug Mode in Production** ✅ FIXED
   - Changed `debug=True` to `debug=False`
   - Added proper host and port configuration

4. **No Version Pins** ✅ FIXED
   - Updated `requirements.txt` with specific versions
   - Added missing `joblib` dependency

5. **Missing Runtime Specification** ✅ FIXED
   - Created `runtime.txt` with Python 3.11.0

---

## 🚀 How to Deploy on Render

### Option 1: Deploy WITHOUT the Large CSV (Recommended for Free Tier)

1. **Update .gitignore** to exclude the CSV:
   ```bash
   echo "reviews.csv" >> .gitignore
   ```

2. **Commit and Push to GitHub**:
   ```bash
   git add .
   git commit -m "Prepare for Render deployment"
   git push origin main
   ```

3. **Create Render Web Service**:
   - Go to https://dashboard.render.com/
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Configure:
     - **Name**: sentiment-analysis-app
     - **Environment**: Python 3
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: Leave empty (uses Procfile)
     - **Instance Type**: Free

4. **Deploy**: Click "Create Web Service"

### Option 2: Deploy WITH the CSV (Requires Paid Plan or Optimization)

If you need the full dataset:

**A. Use a smaller sample:**
```python
# In train_model.py, add this before training:
data = data.sample(n=10000)  # Use only 10,000 rows
```

**B. Or use external storage:**
- Upload CSV to Google Drive/Dropbox
- Modify app.py to download it on startup
- Or use Render PostgreSQL database

---

## 🧪 Test Locally First

Before deploying, test the changes locally:

```bash
# Activate virtual environment
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Test with gunicorn (production server)
gunicorn app:app

# Open browser at http://localhost:8000
```

---

## 📋 Deployment Checklist

- [x] Procfile created
- [x] requirements.txt updated with versions
- [x] runtime.txt created
- [x] app.py configured for production
- [x] .gitignore created
- [ ] Test locally with gunicorn
- [ ] Push to GitHub
- [ ] Create Render service
- [ ] Monitor deployment logs
- [ ] Test deployed app

---

## 🐛 Troubleshooting

### Error: "Application failed to start"
- Check Render logs for specific error
- Verify all dependencies are in requirements.txt
- Ensure model.pkl and vectorizer.pkl are committed to Git

### Error: "Out of memory"
- The reviews.csv (66MB) is too large for free tier
- Exclude it from deployment (see Option 1)
- Or upgrade to paid plan

### Error: "Module not found"
- Add missing module to requirements.txt
- Redeploy

### Error: "Port already in use" (local testing)
- Kill the process using port 5000/8000
- Or use a different port: `gunicorn app:app --bind 0.0.0.0:8080`

---

## 📊 What Happens on Deployment

1. Render clones your GitHub repo
2. Installs Python 3.11.0 (from runtime.txt)
3. Runs: `pip install -r requirements.txt`
4. Starts app with: `gunicorn app:app` (from Procfile)
5. Your app is live! 🎉

---

## 🔗 Useful Links

- [Render Documentation](https://render.com/docs)
- [Flask Deployment Guide](https://flask.palletsprojects.com/en/latest/deploying/)
- [Gunicorn Documentation](https://docs.gunicorn.org/)

---

## 💡 Next Steps After Deployment

1. **Add Environment Variables** (if needed):
   - Go to Render Dashboard → Your Service → Environment
   - Add: `SECRET_KEY`, `DATABASE_URL`, etc.

2. **Set up Custom Domain** (optional):
   - Go to Settings → Custom Domain
   - Add your domain

3. **Monitor Performance**:
   - Check Render Metrics
   - Set up alerts

4. **Enable Auto-Deploy**:
   - Render can auto-deploy on Git push
   - Enable in Settings → Auto-Deploy

---

## ⚠️ Important Notes

- **Free Tier Limitations**:
  - 512 MB RAM
  - App sleeps after 15 min of inactivity
  - First request after sleep takes ~30 seconds

- **Model Files**:
  - Ensure `model.pkl` and `vectorizer.pkl` are in Git
  - They should be ~5MB total (acceptable)

- **Security**:
  - Change default login credentials (admin/admin)
  - Add proper session management
  - Use environment variables for secrets

---

Good luck with your deployment! 🚀
