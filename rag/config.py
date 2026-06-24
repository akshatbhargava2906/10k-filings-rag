import polars as pl

# Used to Cut a sample dataset for quick viewing of the data.

sample = ( 
        pl.scan_parquet("data\data\\001-00000-of-00001-ecbd6ff05ee6eec2.parquet").select(
        ['cik', 'company_name', 'filing_date', 'Business', 
        'Risk Factors', 'Unresolved Staff Comments', 'Properties', 
        'Legal Proceedings', 'Mine Safety Disclosures', 
        'Market for Registrant’s Common Equity, Related Stockholder Matters and Issuer Purchases of Equity Securities', 
        'Selected Financial Data', 'Management’s Discussion and Analysis of Financial Condition and Results of Operations', 
        'Quantitative and Qualitative Disclosures about Market Risk', 'Financial Statements and Supplementary Data', 
        'Changes in and Disagreements with Accountants on Accounting and Financial Disclosure', 'Controls and Procedures', 
        'Other Information', 'Directors, Executive Officers and Corporate Governance', 'Executive Compensation', 
        'Security Ownership of Certain Beneficial Owners and Management and Related Stockholder Matters', 
        'Certain Relationships and Related Transactions, and Director Independence', 'Principal Accountant Fees and Services',
        'Exhibits, Financial Statement Schedules']
    ).head(500)
    .collect()
)
sample.write_parquet("data\sample.parquet")

