# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
from genlayer import *
import json


class MockResolutionListener(gl.Contract):
    last_sub_id: u256
    last_outcome: str
    last_domain: str
    last_issues: u32

    def __init__(self) -> None:
        self.last_sub_id = u256(0)
        self.last_outcome = ""
        self.last_domain = ""
        self.last_issues = u32(0)

    @gl.public.write
    def on_evaluation_done(
        self,
        submission_id: u256,
        actor: Address,
        domain: str,
        final_outcome: str,
        issues_found: u32,
    ) -> None:
        self.last_sub_id = submission_id
        self.last_outcome = final_outcome
        self.last_domain = domain
        self.last_issues = issues_found

    @gl.public.view
    def get_last_event(self) -> str:
        return json.dumps({
            "submission_id": str(self.last_sub_id),
            "outcome": self.last_outcome,
            "domain": self.last_domain,
            "issues": int(self.last_issues),
        })
