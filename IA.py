import heapq

def dijkstra(grafo, inicio, fin):
    """Encuentra la ruta más corta en un grafo usando Dijkstra."""
    cola_prioridad = [(0, inicio, [])]  # (costo, nodo, camino)
    visitados = set()
    
    while cola_prioridad:
        costo, nodo, camino = heapq.heappop(cola_prioridad)
        
        if nodo in visitados:
            continue
        
        camino = camino + [nodo]
        visitados.add(nodo)
        
        if nodo == fin:
            return camino, costo
        
        for vecino, peso in grafo.get(nodo, {}).items():
            if vecino not in visitados:
                heapq.heappush(cola_prioridad, (costo + peso, vecino, camino))
    
    return None, float("inf")  # No hay ruta

# Definición del grafo de transporte
grafo_transporte = {
    'A': {'B': 10, 'C': 15},
    'B': {'D': 12, 'E': 15},
    'C': {'E': 10},
    'D': {'F': 5},
    'E': {'D': 2, 'F': 5},
    'F': {}
}

# Uso del sistema
inicio, fin = 'A', 'F'
ruta, costo = dijkstra(grafo_transporte, inicio, fin)
print(f"Mejor ruta de {inicio} a {fin}: {ruta} con un costo de {costo} minutos")
