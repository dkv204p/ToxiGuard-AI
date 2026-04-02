import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# Apply explicit white color scheme for transparent images
mpl.rcParams.update({
    "text.color": "white",
    "axes.labelcolor": "white",
    "xtick.color": "white",
    "ytick.color": "white",
    "axes.edgecolor": "white"
})

# Load datasets
tox = pd.read_csv('data/cleaned_tox21.csv')
zinc = pd.read_csv('data/zinc250k.csv')

print("Tox21:", tox.shape)
print("ZINC:", zinc.shape)

# Use logP if available
if 'logP' in zinc.columns:
    plt.figure()
    plt.hist(zinc['logP'], bins=50, color='#4361ee')
    plt.title("ZINC logP Distribution")
    plt.xlabel("logP")
    plt.ylabel("Frequency")
    plt.savefig('app/static/zinc_logp.png', transparent=True)
    print("ZINC logP plot saved ✅")

# Count molecules
plt.figure()
plt.bar(['Tox21', 'ZINC'], [len(tox), len(zinc)], color=['#ef4444', '#10b981'])
plt.title("Dataset Size Comparison")
plt.savefig('app/static/dataset_comparison.png', transparent=True)

print("Analysis complete ✅")