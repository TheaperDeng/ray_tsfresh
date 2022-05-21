from tsfresh.utilities.distribution import IterableDistributorBaseClass
import ray

class RayDistributor(IterableDistributorBaseClass):
    def __init__(
        self,
        address=None,
        rayinit_config={},
        n_workers=1,
        disable_progressbar=False,
        progressbar_title="Feature Extraction",
    ):
        ray.init(address=address, **rayinit_config)
        self.n_workers = n_workers
        self.cpu_per_worker = max(1, int(ray.available_resources()['CPU']) // self.n_workers)
        self.disable_progressbar = disable_progressbar
        self.progressbar_title = progressbar_title

    def calculate_best_chunk_size(self, data_length):
        chunk_size, extra = divmod(data_length, self.n_workers * 5)
        if extra:
            chunk_size += 1
        return chunk_size

    def distribute(self, func, partitioned_chunks, kwargs):
        remote_func = ray.remote(func).options(num_cpus=self.cpu_per_worker)
        results = [remote_func.remote(chunk, **kwargs) for chunk in partitioned_chunks]
        for result in results:
            yield ray.get(result)

    def close(self):
        ray.shutdown()
