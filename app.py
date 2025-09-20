#!/usr/bin/env python3
from flask import Flask, jsonify, request

app = Flask(__name__)


def create_orientation_plan(payload: dict) -> dict:
    """Return a canned one-sheet plan for UCLA post-arrival orientation tasks."""
    preferred_name = payload.get("preferred_name") or "Bruin"
    term = payload.get("term") or "upcoming term"

    action_sheet = [
        {
            "task": "Submit Dashew Center online check-in",
            "why": "Confirms visa compliance and activates your SEVIS record.",
            "auto_navigation": {
                "simulate": "Open https://internationalcenter.ucla.edu/services/online-check-in and prefill UID",
                "status": "ready_to_launch"
            },
            "needs_from_you": ["UCLA Logon ID", "I-94 arrival record PDF", "U.S. address"],
            "estimated_time_minutes": 10
        },
        {
            "task": "Upload visa documents to UCLA I-Portal",
            "why": "Required within 10 days of arrival to avoid enrollment holds.",
            "auto_navigation": {
                "simulate": "Navigate to https://iportal.sa.ucla.edu and stage document upload workflow",
                "status": "awaiting_confirmation"
            },
            "needs_from_you": ["Passport ID page", "Signed Form I-20 or DS-2019"],
            "estimated_time_minutes": 8
        },
        {
            "task": "Clear BruinBill balance",
            "why": "Prevents late fees before classes begin.",
            "auto_navigation": {
                "simulate": "Open BruinBill summary and queue ACH payment",
                "status": "requires_final_amount"
            },
            "needs_from_you": ["Payment method confirmation"],
            "estimated_time_minutes": 5
        },
        {
            "task": "Reserve mandatory Dashew live session",
            "why": "Completes post-arrival orientation checklist.",
            "auto_navigation": {
                "simulate": "Book first available orientation session via Dashew Eventbrite",
                "status": "ready_to_launch"
            },
            "needs_from_you": ["Preferred session date"],
            "estimated_time_minutes": 3
        },
        {
            "task": "Submit UCLA immunization & TB screening",
            "why": "Removes Ashe Center health hold before week 3.",
            "auto_navigation": {
                "simulate": "Open https://immunizationrequirement.ucla.edu and stage upload",
                "status": "waiting_for_records"
            },
            "needs_from_you": ["Vaccine records", "TB screening lab results"],
            "estimated_time_minutes": 12
        }
    ]

    references = [
        {
            "title": "Dashew Center Post-Arrival Checklist",
            "url": "https://internationalcenter.ucla.edu/post-arrival"
        },
        {
            "title": "BruinBill Help Center",
            "url": "https://www.finance.ucla.edu/student-finance/bruins-bill"
        },
        {
            "title": "UCLA Immunization Requirement",
            "url": "https://immunizationrequirement.ucla.edu"
        }
    ]

    return {
        "mode": "ask-once-no-chat-demo",
        "title": "UCLA Post-Arrival Orientation Command Sheet",
        "summary": (
            f"Hi {preferred_name}, I can finish the UCLA post-arrival orientation setup for the {term}. "
            "Everything is consolidated into this one confirmation sheet—no back-and-forth chat needed."
        ),
        "assumptions": [
            "You are a newly arrived international student who has already landed in Los Angeles.",
            "Your UCLA Logon ID has been activated.",
            "You can provide identity documents if prompted."
        ],
        "information_to_confirm": [
            {
                "item": "Arrival date",
                "reason": "Needed to verify SEVIS reporting window."
            },
            {
                "item": "Preferred orientation session slot",
                "reason": "Allows auto-booking without further prompts."
            }
        ],
        "action_sheet": action_sheet,
        "automations_ready": [
            {
                "id": "dashew_check_in",
                "description": "Prefill Dashew Center check-in form up to the submission button.",
                "status": "awaiting_single_tap_approval"
            },
            {
                "id": "bruinbill_balance_refresh",
                "description": "Retrieve outstanding balance and draft ACH payment.",
                "status": "awaiting_single_tap_approval"
            }
        ],
        "agent_to_agent_negotiations": [
            {
                "counterparty": "Dashew Center virtual assistant",
                "intent": "Request earlier orientation slot if initial choice is full",
                "status": "auto_escalate_if_needed"
            }
        ],
        "confirmation_prompt": "Ready for me to launch these steps and pause only when manual input is absolutely required?",
        "references": references
    }


def create_default_plan(payload: dict) -> dict:
    """Fallback response when no scenario-specific plan is available."""
    original_request = payload.get("request") or payload.get("scenario") or ""
    return {
        "mode": "ask-once-no-chat-demo",
        "title": "One-shot automation placeholder",
        "summary": (
            "Provide more detail about the process you want automated so I can compile a single "
            "confirmation sheet."
        ),
        "echo": original_request,
        "next_step": "Describe the target service (e.g., university task, travel booking, billing issue)."
    }


@app.route('/one-shot-plan', methods=['POST'])
def one_shot_plan():
    payload = request.get_json(force=True, silent=True) or {}
    description = " ".join(
        str(payload.get(key, "")) for key in ("request", "scenario", "goal", "problem")
    ).lower()

    if "ucla" in description and "orientation" in description:
        plan = create_orientation_plan(payload)
    else:
        plan = create_default_plan(payload)

    return jsonify(plan)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
