from app.search import ImageSearch
import gradio as gr

searcher = ImageSearch()

def search_images(query, top_k):
    results = searcher.execute(query, top_k=top_k)
    if not results:
        return []
    gallery_items = []
    for result in results:
        gallery_items.append((result["image_path"], f"{result['caption']} | Distance: {result['distance']:.3f}"))
    return gallery_items

with gr.Blocks() as demo:
    gr.Markdown("# Semantic Image Search")
    with gr.Row():
        query_input = gr.Textbox(label="Enter your search query",
                                 placeholder="e.g. person holding a snake")
        top_k_input = gr.Slider(label="Number of results", minimum=1, maximum=10, step=1, value=5)
    with gr.Row():
        search_button = gr.Button("Search")
    with gr.Row():
        gallery_output = gr.Gallery(label="Search Results", columns=2)
    
    search_button.click(fn=search_images, inputs=[query_input, top_k_input], outputs=gallery_output)
