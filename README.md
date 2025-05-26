# Portfolio Risk Scoring and Client Profiling

## Project Overview
This project focuses on analyzing and scoring client investment portfolios based on asset distribution, risk exposure, and diversification levels. The goal is to generate actionable insights that support Financial Advisors and Business Strategy Teams in delivering personalized investment strategies, improving client retention, and ensuring compliance with appropriate risk profiles.

## Dataset Information
The dataset contains **100,000 synthetic client records** generated to simulate real-world financial portfolios. Each record includes the following fields:
- **Client_ID**: Unique identifier for each client
- **Equity %**: Percentage of portfolio in equities (stocks)
- **Bond %**: Percentage of portfolio in bonds
- **Cash %**: Percentage of portfolio in cash or equivalents
- **Other Assets %**: Percentage of portfolio in alternative assets

All asset allocations are structured to sum up logically to approximately 100%.

## Tools and Technologies
- **Python** (pandas, numpy, os)
- **CSV file handling**
- **Linux terminal operations** for project setup and management
- (Optional) **Power BI / Matplotlib** for data visualization extensions

## Business Relevance
This project directly aligns with Financial Advisor Business Technology (FABT) functions by:
- Identifying clients' investment risk levels (High, Medium, Low) based on their portfolio structure.
- Scoring the diversification of client portfolios to assess resilience against market volatility.
- Helping Financial Advisors prioritize client engagement strategies tailored to specific risk profiles.
- Enabling Business Teams to target improvement areas in asset allocation recommendations.

By offering structured insights, the project contributes to more personalized, compliant, and data-driven advisory services.

## How to Run

1. Clone the repository.

2. Navigate to the `scripts/` directory:  
cd scripts

3. Generate the synthetic client dataset:  
python3 dataset_generator.py

4. Perform risk scoring and diversification analysis:  
python3 risk_scoring.py

5. The final output file `portfolio_risk_scored.csv` will be created under the `output/` directory.
## Author

**Ahmet Guclu**  
- Senior Business Analyst | Data Analyst  
- LinkedIn: [Ahmet Guclu](https://www.linkedin.com/in/ahmet-guclu-7907992a5/)  
- GitHub: [gucluahmt](https://github.com/gucluahmt)  

---

*This project was developed to demonstrate expertise in Business Analysis, Financial Advisory Technology (FABT) functions, data validation, risk profiling, and client portfolio optimization.*
