from amis import (
    get_model_name,
    sequence_prob,
)


def parse_args():
    import argparse

    parser = argparse.ArgumentParser(
        description="Recommend substitutions to a wildtype sequence"
    )
    parser.add_argument(
        "--sequence",
        type=str,
        default="MSKGEELFFTGVVPILVELDGDVNGHKFSVSGEGEGDATYGKLTLKFICTTGKLPVPWPTLVTTLTGFDSTYGVQCFSRYPDHMKQHDFFKSAMPEGYVQERTIFFKDDGNYKTRAEVKFEGDTLVNRIELKGIDFKEDGNILGHKLEYNYNSHNVYIMADKQKNGIKVNFKIRHNIEDGSVQLADHYQQNTPIGDGPVLLPDNHYLSTQSALSKDPNEKRDHMVLLEFVTAAGITHGMDELYK",
        help="Wildtype sequence",
    )
    parser.add_argument(
        "--model-names",
        type=str,
        default=["esm1b", "esm1v1"],
        # default=[ 'esm1b', 'esm1v1', 'esm1v2', 'esm1v3', 'esm1v4', 'esm1v5', ]
        nargs="+",
        help="Type of language model (e.g., esm1b, esm1v1)",
    )
    parser.add_argument(
        "--alpha", type=float, default=1, help="alpha stringency parameter"
    )
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()

    models = [get_model_name(model_name) for model_name in args.model_names]

    probs = sequence_prob(args.sequence, models, alpha=args.alpha)
    print(probs)
    