#Prerequisites
#pip install chromadb
'''import chromadb

def initialize_knowledge_base():
    client = chromadb.Client()
    collection = client.get_or_create_collection(name="educational_kb")

    educational_docs = [
        {
            "id": "edu_1",
            "content": "Newton's First Law states that an object remains at rest or in uniform motion unless acted upon by an external force.",
            "source": "Physics_101_Textbook.pdf"
        },
        {
            "id": "edu_2",
            "content": "Mitochondria are double-membrane-bound organelles found in most eukaryotic organisms that generate most of the cell's ATP.",
            "source": "Cell_Biology_Notes.docx"
        },
        {
            "id": "edu_3",
            "content": "The French Revolution began in 1789 with the storming of the Bastille and led to the end of the absolute monarchy in France.",
            "source": "World_History_Archive.txt"
        },
        {
            "id": "edu_4",
            "content": "In Python, a dictionary is an unordered, mutable collection that stores data in key-value pairs.",
            "source": "CS101_Python_Guide.md"
        },
        {
            "id": "edu_5",
            "content": "Supply and demand is an economic model of price determination in a market where price settles at equilibrium.",
            "source": "Macroeconomics_Intro.pdf"
        },
        {
            "id": "edu_6",
            "content": "Plate tectonics is the scientific theory explaining the movement of Earth's lithosphere, causing earthquakes and volcanic activity.",
            "source": "Earth_Science_Handbook.pdf"
        },
        {
            "id": "edu_7",
            "content": "DNA replication is the biological process of producing two identical replicas of DNA from one original DNA molecule.",
            "source": "Genetics_Lecture_Slides.pptx"
        },
        {
            "id": "edu_8",
            "content": "The Pythagorean theorem states that in a right triangle, the square of the hypotenuse equals the sum of the squares of the other two sides.",
            "source": "Geometry_Fundamentals.pdf"
        }
    ]

    collection.add(
        documents=[item["content"] for item in educational_docs],
        metadatas=[{"source": item["source"]} for item in educational_docs],
        ids=[item["id"] for item in educational_docs]
    )
    return collection

def main():
    print("Initializing Educational Document Retrieval System...")
    collection = initialize_knowledge_base()
    print("System ready! Type 'exit' to quit.\n")

    while True:
        question = input("Ask a question: ").strip()
        if question.lower() in {"exit", "quit"}:
            print("Exiting retrieval system.")
            break
        if not question:
            continue

        # Retrieve the top 2 most relevant documents
        results = collection.query(
            query_texts=[question],
            n_results=2
        )

        print("\n--- Retrieved Documents ---")
        for i in range(len(results["documents"][0])):
            content = results["documents"][0][i]
            source = results["metadatas"][0][i]["source"]
            distance = results["distances"][0][i]

            print(f"Match {i+1}:")
            print(f"  Content : {content}")
            print(f"  Source  : {source}")
            print(f"  Distance: {distance:.4f}\n")
        print("-" * 40 + "\n")

if __name__ == "__main__":
    main()

'''