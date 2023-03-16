#include "lists.h"

/**
 * print_dlistint - prints all the elements of a dlistint_t list
 * @h: pointer to the head of the list
 *
 * Return: the number of nodes
 *
 * Description: This function prints all the elements of a doubly linked list of
 * integers, starting from the given head pointer. It returns the number of nodes
 * in the list.
 */
size_t print_dlistint(const dlistint_t *h)
{
    size_t count = 0;

    while (h != NULL)
    {
     printf("%d\n", h->n);
     h = h->next;
     count++;
    }

    return (count);
}
