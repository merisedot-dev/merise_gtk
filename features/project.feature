Feature: Creating and managing projects.

    Scenario: A new window does only show a welcome screen
        When we create a new window
        Then no project is loaded
        And the screen showed only has the project logo and version info

    Scenario Outline: Creating project with different target SGBDs.
        Given a new window
        And no project is loaded
        When the user clicks on the "new project" button
        And enters the name "<name>" for the project
        And enters the path "<path>" for the project
        And selects <sgbd> as the target sgbd
        And the user clicks on the "create" button
        Then the window shifts to the project view
        And a new project is on display
        And the project has 0 MCD graphs
        And the project has 0 MLD graphs
        And the project has 0 SQL scripts

        Examples:
            |name|path|sgbd|
