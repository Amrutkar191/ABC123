import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq, left, right)
        heapq.heappush(heap, merged)
    
    return heap[0]

def generate_codes(node, prefix="", codebook=defaultdict(str)):
    if node:
        if node.char is not None:
            codebook[node.char] = prefix
        else:
            generate_codes(node.left, prefix + "0", codebook)
            generate_codes(node.right, prefix + "1", codebook)
    return codebook

def print_huffman_table(frequencies, codebook):
    print(f"{'Symbol':<10}{'Frequency':<10}{'Code':<20}{'Size':<15}")
    print("-" * 55)
    for char, freq in frequencies.items():
        code = codebook[char]
        size = freq * len(code)
        print(f"{char:<10}{freq:<10}{code:<20}{size:<15}")

def huffman_encoding(frequencies):
    root = build_huffman_tree(frequencies)
    codebook = generate_codes(root)
    
    encoded_size = sum(frequencies[char] * len(code) for char, code in codebook.items())
    total_frequency = sum(frequencies.values())
    char_bits = len(frequencies) * 8
    
    average_code_length = sum(frequencies[char] * len(code) for char, code in codebook.items()) / total_frequency if total_frequency else 0
    
    print_huffman_table(frequencies, codebook)
    
    print(f"\nOriginal Size: {char_bits} bits")
    print(f"Encoded Size: {encoded_size} bits")
    print(f"\nCharacter Bits: {char_bits} bits")
    print(f"Total Frequency: {total_frequency} units")
    print(f"Encoded Data Bits: {encoded_size} bits")
    print(f"Total Encoding Size: {char_bits + encoded_size + total_frequency} bits")
    print(f"Average Code Length per Character: {average_code_length:.2f} bits")

if __name__ == "__main__":
    frequencies = {'A': 5, 'B': 1, 'C': 6, 'D': 3}
    huffman_encoding(frequencies)
