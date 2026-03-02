import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import trustworthiness


def main():

    # Load original dataset
    df = pd.read_csv("data/city_lifestyle_dataset.csv")

    # Remove non-numeric columns
    X = df.drop(["city_name", "country"], axis=1)

    # Standardize original data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Load 2D embeddings
    pca_2d = pd.read_csv("outputs/pca_emb_2d.csv").values
    tsne_2d = pd.read_csv("outputs/tsne_emb_2d.csv").values

    # Compute trustworthiness
    pca_score = trustworthiness(X_scaled, pca_2d)
    tsne_score = trustworthiness(X_scaled, tsne_2d)

    print("=== Trustworthiness Comparison ===")
    print(f"PCA   : {pca_score:.4f}")
    print(f"t-SNE : {tsne_score:.4f}")


if __name__ == "__main__":
    main()