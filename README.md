# Sentiment Analysis Web Application

A Flask-based web application for sentiment analysis using Machine Learning.

## Features
- 🔐 User Authentication (Login/Register)
- 🤖 Sentiment Prediction (Positive/Negative)
- 📊 Interactive Dashboard with Analytics
- 📈 Data Visualizations

## Tech Stack
- **Backend**: Flask (Python)
- **ML Model**: Scikit-learn (Naive Bayes + TF-IDF)
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Render (with Gunicorn)

## Local Development

### Prerequisites
- Python 3.9+
- pip

### Installation

1. Clone the repository
```bash
git clone <your-repo-url>
cd vectorizer
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the application
```bash
python app.py
```

5. Open browser at `http://localhost:5000`

## Deployment on Render

### Important Notes:
- The `reviews.csv` file (66MB) is too large for free deployment
- **Option 1**: Exclude it from Git and use dummy data (already handled in code)
- **Option 2**: Use a smaller sample dataset
- **Option 3**: Store data in a database (PostgreSQL on Render)

### Steps:

1. **Push to GitHub** (if not already done)
```bash
git add .
git commit -m "Prepare for Render deployment"
git push origin main
```

2. **Create Render Web Service**
   - Go to [Render Dashboard](https://dashboard.render.com/)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Configure:
     - **Name**: sentiment-analysis-app
     - **Environment**: Python 3
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app` (from Procfile)
     - **Instance Type**: Free

3. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment to complete

### Environment Variables (Optional)
If you need to add any secrets:
- Go to your service → Environment
- Add variables like `SECRET_KEY`, `DATABASE_URL`, etc.

## Project Structure
```
vectorizer/
├── app.py                 # Main Flask application
├── train_model.py         # ML model training script
├── model.pkl              # Trained model
├── vectorizer.pkl         # TF-IDF vectorizer
├── requirements.txt       # Python dependencies
├── Procfile              # Render deployment config
├── reviews.csv           # Dataset (large - optional)
├── static/               # CSS, images, charts
├── templates/            # HTML templates
└── venv/                 # Virtual environment (excluded)
```

## Default Login Credentials
- **Username**: admin
- **Password**: admin

## Known Issues & Solutions

### Issue: Large CSV File (66MB)
**Solution**: The app now handles missing CSV gracefully by using dummy data. For production:
- Use a database (PostgreSQL)
- Or upload CSV to cloud storage (S3, Google Cloud Storage)
- Or use a smaller sample dataset

### Issue: Render Free Tier Limitations
- 512MB RAM limit
- May need to optimize model size
- Consider using model compression techniques

## Future Improvements
- [ ] Add user database (SQLite/PostgreSQL)
- [ ] Implement proper authentication with sessions
- [ ] Add API endpoints for predictions
- [ ] Optimize model size
- [ ] Add more visualizations
- [ ] Implement real-time predictions

## License
MIT License
