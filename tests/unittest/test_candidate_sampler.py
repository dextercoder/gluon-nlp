import mxnet as mx
import pytest

from gluonnlp.data.candidate_sampler import UnigramCandidateSampler


@pytest.mark.seed(1)
def test_unigram_candidate_sampler():
    N = 1000
    sampler = UnigramCandidateSampler(mx.nd.arange(N))
    sampled = sampler(3)
    assert all(mx.nd.array([523, 729, 698]) == sampled)
