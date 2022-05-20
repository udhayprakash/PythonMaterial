Fixtures 
---------
- fixtures are reusable, fixtures are implemented in a modular manner, so each fixture name triggers a fixture function.
- fixtures can use other fixtures.
- test or fixture can request more than one fixture at a time.
- fixtures can be auto-used, sometimes there can be fixtures that might need by all the test cases, in that case, we can use the “Auto use” fixture. eg: @pytest.fixture(autouse=True) .
- fixture management scales from simple unit tests to complex functional testing. We can even parameterize fixtures and tests according to configuration and component options.
- tear down logic can be easily managed no matter how many fixtures are used.
- Fixture scopes can be set for each fixture which will helps tremendously in saving a lot of time and computing resources while running expensive test cases.