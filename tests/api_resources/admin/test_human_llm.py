# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from structify import Structify, AsyncStructify
from tests.utils import assert_matches_type
from structify.types import ExecutionStep
from structify.types.admin import (
    StepChoices,
    HumanLlmPrelabelStepResponse,
    HumanLlmGetQueuedJobsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHumanLlm:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_next_step(self, client: Structify) -> None:
        human_llm = client.admin.human_llm.get_next_step(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExecutionStep, human_llm, path=["response"])

    @parametrize
    def test_raw_response_get_next_step(self, client: Structify) -> None:
        response = client.admin.human_llm.with_raw_response.get_next_step(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        human_llm = response.parse()
        assert_matches_type(ExecutionStep, human_llm, path=["response"])

    @parametrize
    def test_streaming_response_get_next_step(self, client: Structify) -> None:
        with client.admin.human_llm.with_streaming_response.get_next_step(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            human_llm = response.parse()
            assert_matches_type(ExecutionStep, human_llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_queued_jobs(self, client: Structify) -> None:
        human_llm = client.admin.human_llm.get_queued_jobs()
        assert_matches_type(HumanLlmGetQueuedJobsResponse, human_llm, path=["response"])

    @parametrize
    def test_raw_response_get_queued_jobs(self, client: Structify) -> None:
        response = client.admin.human_llm.with_raw_response.get_queued_jobs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        human_llm = response.parse()
        assert_matches_type(HumanLlmGetQueuedJobsResponse, human_llm, path=["response"])

    @parametrize
    def test_streaming_response_get_queued_jobs(self, client: Structify) -> None:
        with client.admin.human_llm.with_streaming_response.get_queued_jobs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            human_llm = response.parse()
            assert_matches_type(HumanLlmGetQueuedJobsResponse, human_llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_prelabel_step(self, client: Structify) -> None:
        human_llm = client.admin.human_llm.prelabel_step(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(HumanLlmPrelabelStepResponse, human_llm, path=["response"])

    @parametrize
    def test_raw_response_prelabel_step(self, client: Structify) -> None:
        response = client.admin.human_llm.with_raw_response.prelabel_step(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        human_llm = response.parse()
        assert_matches_type(HumanLlmPrelabelStepResponse, human_llm, path=["response"])

    @parametrize
    def test_streaming_response_prelabel_step(self, client: Structify) -> None:
        with client.admin.human_llm.with_streaming_response.prelabel_step(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            human_llm = response.parse()
            assert_matches_type(HumanLlmPrelabelStepResponse, human_llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_prelabel_step(self, client: Structify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_id` but received ''"):
            client.admin.human_llm.with_raw_response.prelabel_step(
                "",
            )

    @parametrize
    def test_method_start_next_job(self, client: Structify) -> None:
        human_llm = client.admin.human_llm.start_next_job()
        assert_matches_type(StepChoices, human_llm, path=["response"])

    @parametrize
    def test_method_start_next_job_with_all_params(self, client: Structify) -> None:
        human_llm = client.admin.human_llm.start_next_job(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(StepChoices, human_llm, path=["response"])

    @parametrize
    def test_raw_response_start_next_job(self, client: Structify) -> None:
        response = client.admin.human_llm.with_raw_response.start_next_job()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        human_llm = response.parse()
        assert_matches_type(StepChoices, human_llm, path=["response"])

    @parametrize
    def test_streaming_response_start_next_job(self, client: Structify) -> None:
        with client.admin.human_llm.with_streaming_response.start_next_job() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            human_llm = response.parse()
            assert_matches_type(StepChoices, human_llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_step(self, client: Structify) -> None:
        human_llm = client.admin.human_llm.update_step(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tool_calls=[
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
            ],
        )
        assert_matches_type(StepChoices, human_llm, path=["response"])

    @parametrize
    def test_raw_response_update_step(self, client: Structify) -> None:
        response = client.admin.human_llm.with_raw_response.update_step(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tool_calls=[
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        human_llm = response.parse()
        assert_matches_type(StepChoices, human_llm, path=["response"])

    @parametrize
    def test_streaming_response_update_step(self, client: Structify) -> None:
        with client.admin.human_llm.with_streaming_response.update_step(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tool_calls=[
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            human_llm = response.parse()
            assert_matches_type(StepChoices, human_llm, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncHumanLlm:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get_next_step(self, async_client: AsyncStructify) -> None:
        human_llm = await async_client.admin.human_llm.get_next_step(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExecutionStep, human_llm, path=["response"])

    @parametrize
    async def test_raw_response_get_next_step(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.human_llm.with_raw_response.get_next_step(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        human_llm = await response.parse()
        assert_matches_type(ExecutionStep, human_llm, path=["response"])

    @parametrize
    async def test_streaming_response_get_next_step(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.human_llm.with_streaming_response.get_next_step(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            human_llm = await response.parse()
            assert_matches_type(ExecutionStep, human_llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_queued_jobs(self, async_client: AsyncStructify) -> None:
        human_llm = await async_client.admin.human_llm.get_queued_jobs()
        assert_matches_type(HumanLlmGetQueuedJobsResponse, human_llm, path=["response"])

    @parametrize
    async def test_raw_response_get_queued_jobs(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.human_llm.with_raw_response.get_queued_jobs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        human_llm = await response.parse()
        assert_matches_type(HumanLlmGetQueuedJobsResponse, human_llm, path=["response"])

    @parametrize
    async def test_streaming_response_get_queued_jobs(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.human_llm.with_streaming_response.get_queued_jobs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            human_llm = await response.parse()
            assert_matches_type(HumanLlmGetQueuedJobsResponse, human_llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_prelabel_step(self, async_client: AsyncStructify) -> None:
        human_llm = await async_client.admin.human_llm.prelabel_step(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(HumanLlmPrelabelStepResponse, human_llm, path=["response"])

    @parametrize
    async def test_raw_response_prelabel_step(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.human_llm.with_raw_response.prelabel_step(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        human_llm = await response.parse()
        assert_matches_type(HumanLlmPrelabelStepResponse, human_llm, path=["response"])

    @parametrize
    async def test_streaming_response_prelabel_step(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.human_llm.with_streaming_response.prelabel_step(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            human_llm = await response.parse()
            assert_matches_type(HumanLlmPrelabelStepResponse, human_llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_prelabel_step(self, async_client: AsyncStructify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `step_id` but received ''"):
            await async_client.admin.human_llm.with_raw_response.prelabel_step(
                "",
            )

    @parametrize
    async def test_method_start_next_job(self, async_client: AsyncStructify) -> None:
        human_llm = await async_client.admin.human_llm.start_next_job()
        assert_matches_type(StepChoices, human_llm, path=["response"])

    @parametrize
    async def test_method_start_next_job_with_all_params(self, async_client: AsyncStructify) -> None:
        human_llm = await async_client.admin.human_llm.start_next_job(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(StepChoices, human_llm, path=["response"])

    @parametrize
    async def test_raw_response_start_next_job(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.human_llm.with_raw_response.start_next_job()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        human_llm = await response.parse()
        assert_matches_type(StepChoices, human_llm, path=["response"])

    @parametrize
    async def test_streaming_response_start_next_job(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.human_llm.with_streaming_response.start_next_job() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            human_llm = await response.parse()
            assert_matches_type(StepChoices, human_llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_step(self, async_client: AsyncStructify) -> None:
        human_llm = await async_client.admin.human_llm.update_step(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tool_calls=[
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
            ],
        )
        assert_matches_type(StepChoices, human_llm, path=["response"])

    @parametrize
    async def test_raw_response_update_step(self, async_client: AsyncStructify) -> None:
        response = await async_client.admin.human_llm.with_raw_response.update_step(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tool_calls=[
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        human_llm = await response.parse()
        assert_matches_type(StepChoices, human_llm, path=["response"])

    @parametrize
    async def test_streaming_response_update_step(self, async_client: AsyncStructify) -> None:
        async with async_client.admin.human_llm.with_streaming_response.update_step(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            step_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tool_calls=[
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
                {
                    "input": {"save": {}},
                    "name": "Save",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            human_llm = await response.parse()
            assert_matches_type(StepChoices, human_llm, path=["response"])

        assert cast(Any, response.is_closed) is True