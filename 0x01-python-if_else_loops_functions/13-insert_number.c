#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new;
    listint_t *current, *actual, *siguiente;
    int temp = 0;

    current = *head;
    actual = *head;
    siguiente = *head;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = number;
    new->next = NULL;

    if (*head == NULL)
        *head = new;
    else
    {
        while (current->next != NULL)
        {
            current = current->next;
        }
        current->next = new;
    }
    while(actual != NULL)
    {
      siguiente = actual->next;
      while(siguiente != NULL)
      {
        if (actual->n > siguiente->n)
        {
          temp = actual->n;
          actual->n = siguiente->n;
          siguiente->n = temp;
        }
        siguiente = siguiente->next;
      }
      actual = actual->next;
    }
    return (actual);
}