from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from pathlib import Path

## FastAPI app setup

app = FastAPI()
BASE_DIR = Path(__file__).resolve().parent

app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

## Template Routes

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/compound", response_class=HTMLResponse)
async def compound_interest(request: Request):
    return templates.TemplateResponse("compound.html", {"request": request})

@app.get("/mortgage", response_class=HTMLResponse)
async def mortgage(request: Request):
    return templates.TemplateResponse("mortgage.html", {"request": request})

@app.get("/tax", response_class=HTMLResponse)
async def tax(request: Request):
    return templates.TemplateResponse("tax.html", {"request": request})


## Models & Endpoints 

class CompoundRequest(BaseModel):
    principal: float    # Initial amount
    rate: float         # Annual interest rate (percent)
    time: int           # Years
    n: int              # Compounding frequency per year

@app.post("/api/compound")
async def calculate_compound(req: CompoundRequest):
    '''Calculate compound interest using the formula A = P(1 + r/n)^(nt)'''
    P, r, t, n = req.principal, req.rate / 100, req.time, req.n
    A = P * (1 + r / n) ** (n * t)
    I = A - P
    return {"amount": round(A, 2), "interest": round(I, 2)}


class MortgageRequest(BaseModel):
    principal: float       # Loan amount
    rate: float            # Annual interest rate (percent)
    time: int              # Years
    extra_payment: float = 0.0  # Extra monthly payment

@app.post("/api/mortgage")
async def calculate_mortgage(req: MortgageRequest):
    '''Calculate monthly mortgage payment using the formula M = P[r(1 + r)^n] / [(1 + r)^n - 1]'''
    P, monthly_rate, months, e = (
        req.principal,
        req.rate / 100 / 12,
        req.time * 12,
        req.extra_payment,
    )

    m = (P * monthly_rate) / (1 - (1 + monthly_rate) ** -months)
    
    # Initialize variables
    principal_balance = P
    total_interest = 0
    num_payments = 0

    # Loop through monthly payments until the loan is paid off
    while principal_balance > 0:
        interest_payment = principal_balance * monthly_rate
        principal_payment = m - interest_payment + e  # Apply extra payment to principal
        
        # If the remaining balance is less than the principal payment, adjust the final payment
        if principal_balance < principal_payment:
            principal_payment = principal_balance
            
        principal_balance -= principal_payment
        total_interest += interest_payment
        num_payments += 1

    total = P + total_interest

    return {
        "monthly_payment": round(m, 2),
        "total_payment": round(total, 2),
        "total_interest": round(total_interest, 2),
    }


class TaxRequest(BaseModel):
    income: float
    deductions: float
    tax_rate: float  # percent

@app.post("/api/tax")
async def calculate_tax(req: TaxRequest):
    '''Calculate tax owed using the formula Tax = (Income - Deductions) * (Tax Rate / 100)'''
    taxable = max(req.income - req.deductions, 0)
    owed = taxable * (req.tax_rate / 100)
    return {
        "taxable_income": round(taxable, 2),
        "tax_owed": round(owed, 2),
    }