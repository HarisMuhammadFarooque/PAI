import numpy as np

def simulate(seed, n=1000, mu=50, sigma=10):
    rng = np.random.default_rng(seed)
    data = rng.normal(loc=mu, scale=sigma, size=n)

    mean = data.mean()
    median = np.median(data)
    std = data.std(ddof=1)          
    minimum = data.min()
    maximum = data.max()

    within = np.abs(data - mean) <= std
    pct_within = within.mean() * 100

    return {
        "Mean": mean,
        "Median": median,
        "Std Dev": std,
        "Min": minimum,
        "Max": maximum,
        "% within 1 std": pct_within,
    }

results = {}
for seed in (42, 123):
    results[seed] = simulate(seed)
    print(f"--- Seed {seed} ---")
    for k, v in results[seed].items():
        print(f"{k:>15}: {v:.4f}")
    print()

print("--- Comparison (seed 42 vs seed 123) ---")
for k in results[42]:
    a, b = results[42][k], results[123][k]
    print(f"{k:>15}: {a:9.4f} | {b:9.4f} | diff = {abs(a - b):.4f}")