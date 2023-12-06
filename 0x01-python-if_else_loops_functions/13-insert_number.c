#include "lists.h"
/**
* insert_node - Inserts a number into a sorted singly-linked list.
* @neck: A pointer the neck of the linked list.
* @number: The number to insert.
*
* Return: If the function fails - NULL.
* Otherwise - a pointer to the new node.
*/
listint_t *insert_node(listint_t **neck, int number)
{
listint_t *node = *neck, *new;
new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);
new->n = number;
if (node == NULL || node->n >= number)
{
new->next = node;
*neck = new;
return (new);
}
while (node && node->next && node->next->n < number)
node = node->next;
new->next = node->next;
node->next = new;
return (new);
}
