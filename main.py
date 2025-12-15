# Файл: main.py
# Копирай това съдържание в GitHub

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from scraper import DropsTabScraper
from analyzer import CryptoAnalyzer
from formatter import TelegramFormatter

def main():
    # Get language from command line (default: en)
    lang = sys.argv[1] if len(sys.argv) > 1 else 'en'
    
    print(f"🚀 Starting DropsTab analysis (language: {lang})...\n")
    
    # Step 1: Scrape data
    print("📡 Scraping DropsTab...")
    scraper = DropsTabScraper()
    coins = scraper.get_vwap_data()
    sentiment = scraper.get_market_sentiment()
    
    # Exit if scraping failed
    if not coins:
        print("\n" + "="*50)
        print("❌ CRITICAL ERROR: Failed to scrape DropsTab!")
        print("="*50)
        print("\nPossible reasons:")
        print("• No internet connection")
        print("• DropsTab is down")
        print("• DropsTab blocked the scraper")
        print("• HTML structure changed\n")
        print("⚠️  Cannot generate analysis without real data.")
        print("Please check your connection and try again later.\n")
        sys.exit(1)
    
    print(f"✅ Successfully scraped {len(coins)} coins\n")
    
    # Step 2: Analyze
    print("🔍 Analyzing opportunities...")
    analyzer = CryptoAnalyzer()
    opportunities = analyzer.filter_opportunities(coins)
    
    if not opportunities:
        print("\n" + "="*50)
        print("⚠️  WARNING: No opportunities found!")
        print("="*50)
        print("\nNo coins match the criteria:")
        print("• VWAP Score: -85 to -100")
        print("• Bullish Trend: 20-50\n")
        print("This might mean:")
        print("• Market is not in buy zone")
        print("• Wait for better opportunities\n")
        
        # Still generate analysis with available data
        print("Generating analysis with market sentiment only...\n")
    else:
        print(f"✅ Found {len(opportunities)} opportunities\n")
    
    # Step 3: Format for Telegram
    print("📝 Generating Telegram post...")
    formatter = TelegramFormatter()
    telegram_post = formatter.format_analysis(sentiment, opportunities, lang)
    
    # Output
    print("\n" + "="*50)
    print(telegram_post)
    print("="*50 + "\n")
    
    # Save to file
    filename = f"analysis_{lang}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(telegram_post)
    
    print(f"💾 Saved to {filename}")
    print("✅ Analysis complete!\n")
    print("📋 Next steps:")
    print("1. Review the analysis above")
    print("2. Copy content from analysis_{}.txt".format(lang))
    print("3. Paste into your Telegram channel\n")

if __name__ == '__main__':
    main()
