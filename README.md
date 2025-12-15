# Файл: README.md
# Копирай това съдържание в GitHub

# 🌍 DropsTab Global Analyzer

Multilingual crypto analysis tool with automated DropsTab web scraping.

## 🎯 Features

- 🌐 **9 Languages**: EN, BG, RU, ES, TR, DE, AR, ZH, HI
- 🤖 **Automated Scraping**: Real-time data from DropsTab
- 📊 **Smart Analysis**: VWAP, Bullish Trend, Accumulation
- 📱 **Telegram Ready**: Professional formatted posts
- ✅ **No Demo Data**: Only real market data

## 🚀 Installation (UserLand/Alpine Linux)

```bash
# Install dependencies
apk add python3 py3-pip
pip3 install -r requirements.txt

# Clone repo
git clone https://github.com/YOUR_USERNAME/dropstab-global-analyzer.git
cd dropstab-global-analyzer
```

## 💻 Usage

```bash
# English analysis
python3 main.py en

# Bulgarian analysis
python3 main.py bg

# Russian analysis
python3 main.py ru

# Spanish analysis
python3 main.py es
```

Output will be displayed in terminal and saved to `analysis_{lang}.txt`

## 📋 Supported Languages

- 🇬🇧 English (en)
- 🇧🇬 Български (bg)
- 🇷🇺 Русский (ru)
- 🇪🇸 Español (es)
- 🇹🇷 Türkçe (tr)
- 🇩🇪 Deutsch (de)
- 🇸🇦 العربية (ar)
- 🇨🇳 中文 (zh)
- 🇮🇳 हिन्दी (hi)

## ⚙️ How It Works

1. **Scrapes** DropsTab.com for live market data
2. **Analyzes** coins based on VWAP (-85 to -100) and Bullish Trend (20-50)
3. **Filters** top 5 opportunities by score
4. **Formats** professional Telegram post
5. **Outputs** in your chosen language

## 📊 Analysis Criteria

### VWAP Score
- **-85 to -100**: Oversold (buy zone)
- **20-50**: Starting bullish momentum

### Filters
- Only coins matching BOTH criteria
- Ranked by score (|VWAP| + Bullish)
- Top 5 opportunities

## ⚠️ Important Notes

- **NO demo data** - only real scraping
- If scraping fails, program exits with error
- Check internet connection before running
- Review analysis before posting to Telegram

## 🛠️ Troubleshooting

### Scraping Failed Error

**Possible causes:**
- No internet connection
- DropsTab changed HTML structure
- DropsTab blocking requests

**Solutions:**
1. Check internet: `ping dropstab.com`
2. Wait a few minutes and retry
3. Update scraper.py selectors if HTML changed

### No Opportunities Found

**This is normal!** It means:
- Market is not in oversold zone
- No coins match criteria
- Wait for better market conditions

## 📝 License

MIT License - Free to use

## 🔗 Links

- Telegram: @DropsTabGlobal
- DropsTab: https://dropstab.com

---

Made with ❤️ for global crypto community
