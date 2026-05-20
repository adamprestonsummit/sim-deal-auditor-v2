# 📱 SIM Deal Auditor

Automated SIM-only deal scraper across **uSwitch**, **MoneySuperMarket**, and **CompareTheMarket**.  
Outputs a colour-coded Excel file matching your audit format.

---

## 🚀 Deploy to Railway (Free, ~15 minutes, actually works)

### Step 1 — Create a GitHub account
Go to [github.com](https://github.com) and sign up if you don't have one.

### Step 2 — Create a new repository
1. Click **+** (top right) → **New repository**
2. Name it `sim-deal-auditor`
3. Set to **Public**
4. Click **Create repository**

### Step 3 — Upload all files
Click **Add file** → **Upload files** and upload every file in this folder:
- `app.py`
- `requirements.txt`
- `railway.toml`
- `install_browsers.py`

Also create a `.streamlit` folder and upload `config.toml` inside it.

Click **Commit changes**.

### Step 4 — Deploy on Railway
1. Go to [railway.app](https://railway.app) and sign up with your GitHub account (free)
2. Click **New Project**
3. Choose **Deploy from GitHub repo**
4. Select your `sim-deal-auditor` repository
5. Railway detects it automatically — click **Deploy**
6. Wait ~3 minutes for the build (it installs Chromium properly this time)
7. Once deployed, click **Settings** → **Networking** → **Generate Domain**
8. You get a permanent URL like `sim-deal-auditor.up.railway.app`

✅ Bookmark that URL — it works from any browser, any device.

---

## 🖥️ How to use the app

1. Select **contract lengths** — 1M, 12M, 24M (or all three)
2. Set your **price range** — e.g. £5 to £20
3. Click **Start Audit**
4. The app visits each site with a real browser and extracts deals
5. Click **Download Excel** — colour-coded file ready to use

---

## 📊 Excel output format

- One sheet per contract length (1M, 12M, 24M)
- Three side-by-side tables: uSwitch | MoneySuperMarket | CompareTheMarket
- Rows = price points (£5–£20), Columns = networks
- 🟢 Green = best data at that price, 🟡 Amber = mid, 🔴 Red = worst
- Unlimited always green

---

## 💰 Railway free tier limits

Railway's free tier gives you $5 of credit per month — enough for ~500 hours of running time.  
The app only uses compute when someone is actively using it, so in practice this is plenty for weekly audits.  
If you hit the limit, the Hobby plan is £5/month.

---

## 🔄 Updating the app

Edit files in GitHub → Railway auto-redeploys within ~3 minutes.
