from app.schemas import UserCreate

USER_EXAMPLES = {
    "alex": {
        "summary": "User alex",
        "description": "Synthetic user",
        "value": UserCreate(
            name="aaa",
            username="alex",
            password="alex_password",
            email="alex@example.com",
        ),
    },
    "bob": {
        "summary": "User bob",
        "description": "Synthetic user",
        "value": UserCreate(
            name="bbb",
            username="bob",
            password="bob_password",
            email="bob@example.com",
        ),
    },
    "mark": {
        "summary": "User mark",
        "description": "Synthetic user",
        "value": UserCreate(
            name="mmm",
            username="mark",
            password="mark_password",
            email="mark@example.com",
        ),
    },
}
