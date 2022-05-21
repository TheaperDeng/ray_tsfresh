# Distributed tsfresh on Ray
This repo involves a new `RayDistributor` for tsfresh to use ray to distribute the calculations.

`RayDistributor` is a subclass of `IterableDistributorBaseClass` in tsfresh which follows the developing instruction in https://tsfresh.readthedocs.io/en/latest/text/tsfresh_on_a_cluster.html.

## Quick Start
Use `RayDistributor` the same way as `MultiprocessingDistributor`, `ClusterDaskDistributor` or `LocalDaskDistributor`.
```python
from ray_tsfresh import RayDistributor

distributor = RayDistributor(n_workers=8)
# ...
extracted_features = extract_features(..., distributor=distributor)
# ...
```
