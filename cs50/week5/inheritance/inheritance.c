// Simulate genetic inheritance of blood type

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Each person has two parents and two alleles
typedef struct person
{
    struct person *parents[2];
    char alleles[2];
}
person;

const int GENERATIONS = 3;
const int INDENT_LENGTH = 4;

person *create_family(int generations);
void print_family(person *p, int generation);
void free_family(person *p);
char random_allele();


int main(void)
{
    // Seed random number generator
    srand(time(0));

    // Create a new family with three generations
    person *p = create_family(GENERATIONS);

    // Print family tree of blood types
    print_family(p, 0);

    // Free memory
    free_family(p);
}


// Create a new individual with `generations`
person *create_family(int generations)
{
    // Constant: Number of parents.
    int PARENT_TOTAL = 2;

    // Allocate new person memory for use after function call.
    person *new_person = malloc(sizeof(person));

    // Recursive case: If there are still generations left to create,
    if (generations > 1)
    {
        // Create variables for each new parent and inherited allele.
        person *new_parent[PARENT_TOTAL];
        int inherited;

        // For each new parent,
        for (int i = 0; i < PARENT_TOTAL; i++)
        {
            // Recursively call create_family() to create previous generation.
            new_parent[i] = create_family(generations - 1);

            // Assign parent to new_person.
            new_person->parents[i] = new_parent[i];

            // Randomly assign new_person allele from parent alleles.
            inherited = rand() % 2;
            new_person->alleles[i] = new_parent[i]->alleles[inherited];
        }
    }

    // Base case: When there are no additional generations to create,
    else
    {
        // For each new parent,
        for (int i = 0; i < PARENT_TOTAL; i++)
        {
            // Set parent pointer to NULL.
            new_person->parents[i] = NULL;

            // Since parent is NULL, randomly assign "inherited" allele.
            new_person->alleles[i] = random_allele();
        }
    }

    // Return newly created person.
    return new_person;
}


// Free `p` and all ancestors of `p`.
void free_family(person *p)
{
    // Base case: If both parents = NULL, free person
    if ()
    {

    }















    // TODO: Free parents recursively














    // TODO: Free child












}


// Print each family member and their alleles.
void print_family(person *p, int generation)
{
    // Handle base case
    if (p == NULL)
    {
        return;
    }

    // Print indentation
    for (int i = 0; i < generation * INDENT_LENGTH; i++)
    {
        printf(" ");
    }

    // Print person
    if (generation == 0)
    {
        printf("Child (Generation %i): blood type %c%c\n", generation, p->alleles[0], p->alleles[1]);
    }
    else if (generation == 1)
    {
        printf("Parent (Generation %i): blood type %c%c\n", generation, p->alleles[0], p->alleles[1]);
    }
    else
    {
        for (int i = 0; i < generation - 2; i++)
        {
            printf("Great-");
        }
        printf("Grandparent (Generation %i): blood type %c%c\n", generation, p->alleles[0], p->alleles[1]);
    }

    // Print parents of current generation
    print_family(p->parents[0], generation + 1);
    print_family(p->parents[1], generation + 1);
}


// Randomly chooses a blood type allele.
char random_allele()
{
    int r = rand() % 3;
    if (r == 0)
    {
        return 'A';
    }
    else if (r == 1)
    {
        return 'B';
    }
    else
    {
        return 'O';
    }
}
