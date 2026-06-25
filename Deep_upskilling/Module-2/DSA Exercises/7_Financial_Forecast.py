def forecast(amount, rate, years):

    if years == 0:
        return amount

    return forecast(
        amount + amount * rate / 100,
        rate,
        years - 1
    )


principal = float(input("Enter Initial Amount: "))
growth_rate = float(input("Enter Growth Rate (%): "))
years = int(input("Enter Number of Years: "))

future_amount = forecast(
    principal,
    growth_rate,
    years
)

print("Predicted Future Value =", round(future_amount, 2))