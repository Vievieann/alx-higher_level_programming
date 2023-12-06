#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        last_num = (-number % 10)
    elif number >= 0:
        last_num = number % 10
    print("{:d}".format(last_num), end="")
    return last_num

#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @neck: A pointer the head of the linked list.
 * @numero: The number to insert.
 *
 * Return: If the function fails - NULL.
 * Otherwise - a pointer to the new node.
 */

listint_t *insert_node(listint_t **neck, int numero)

{
    listint_t *node = *neck, *new;

        new = malloc(sizeof(listint_t));
        if (new == NULL)
                return (NULL);
        new->n = numero;

        if (node == NULL || node->n >= numero)
        {
                new->next = node;
                *neck = new;
                return (new);
        }

        while (node && node->next && node->next->n < numero)
                node = node->next;

        new->next = node->next;
        node->next = new;

        return (new);
}
