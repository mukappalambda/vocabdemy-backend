## Unreleased

### Feat

- add the delete_user endpoint
- add the update_user endpoint
- add the create_user endpoint
- add the read_user endpoint
- add the read_users endpoint
- add pylint good names
- **app.tests.test_vocab**: add a test for the delete vocab endpoint
- **app.routers.vocab**: add the delete endpoint for vocabs
- **app.controllers.vocab**: add the delete method
- **app.tests.test_vocab**: add a test for the update vocab endpoint
- **app.routers.vocab**: add the update endpoint for vocabs
- **app.controllers.vocab**: add the update method
- **app.schema.vocab**: add UpdateVocabObject
- **app.routers.vocab**: modify the arguements of get_controller method
- **app.dependencies.controller**: use new get_db_session function instead
- **app.dependencies.db_session**: add the get_db_session dep
- add the vocabs post endpoint and test.
- add the basic code structure.
- add basic models.

### Fix

- **poetry**: address the poetry error: "does not contain any element"
- Add the missing pytest library
- **endpoint**: fix vocab linting
- add Optional to the function signature
- disable broad exception
- **app.controller.vocab**: add missing Vocab at a query

### Refactor

- tweak the project directory layout
- **app.database**: extract init proceduce to a function
- **app.schema.vocab**: remove the unused import
- folder structure
