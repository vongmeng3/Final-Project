import os
import tkinter as tk
from tkinter import messagebox, ttk, scrolledtext
from PIL import Image, ImageTk
import csv
import webbrowser

# Import the travel data module
from travel_data import (
    format_travel_info, get_activities_by_type,
    search_activities, get_all_available_activities
)

# Determine the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to your CSV file
DATA_FILE = os.path.join(script_dir, "places.csv")

# Image display size
IMAGE_WIDTH = 400   
IMAGE_HEIGHT = 300

class TravelGuideApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome To Cambodia Travel Guide")
        self.root.geometry("1100x800")  # Made wider to accommodate new features
        self.root.configure(bg='#f0f0f0')
        
        # Set minimum window size
        self.root.minsize(900, 600)
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create main places tab
        self.places_frame = tk.Frame(self.notebook, bg='#f0f0f0')
        self.notebook.add(self.places_frame, text="📍 Places")
        
        # Create travel info tab
        self.info_frame = tk.Frame(self.notebook, bg='#f0f0f0')
        self.notebook.add(self.info_frame, text="ℹ️ Travel Info")
        
        # Initialize main places tab
        self.setup_places_tab()
        
        # Initialize travel info tab
        self.setup_info_tab()
        
        # Load data and initialize
        self.places = self.load_places(DATA_FILE)
        self.filtered_places = self.places
        self.index = 0
        self.current_map_url = None
        
        self.update_list()
        self.update_stats()
        
        # Show first place if available
        if self.filtered_places:
            self.place_listbox.selection_set(0)
            self.show_place()
                    

    def setup_places_tab(self):
        """Setup the main places tab (original functionality)"""
        # Title
        self.title_label = tk.Label(self.places_frame, text="🇰🇭 Welcome To Cambodia Travel Guide 🇰🇭", 
                                   font=("Helvetica", 20, "bold"), bg='#f0f0f0', fg='#2c3e50')
        self.title_label.pack(pady=(0, 20))
        
        # Search section
        self.search_frame = tk.Frame(self.places_frame, bg='#f0f0f0')
        self.search_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.search_label = tk.Label(self.search_frame, text="🔍 Search Places:", 
                                   font=("Helvetica", 12, "bold"), bg='#f0f0f0')
        self.search_label.pack(anchor=tk.W)
        
        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.update_list)
        
        self.search_entry = tk.Entry(self.search_frame, textvariable=self.search_var, 
                                   font=("Helvetica", 11), width=50)
        self.search_entry.pack(fill=tk.X, pady=(5, 0))
        
        # Content frame
        self.content_frame = tk.Frame(self.places_frame, bg='#f0f0f0')
        self.content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Left panel for list
        self.left_panel = tk.Frame(self.content_frame, bg='#f0f0f0', width=300)
        self.left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        self.left_panel.pack_propagate(False)
        
        self.list_label = tk.Label(self.left_panel, text="📍 Places to Visit:", 
                                 font=("Helvetica", 12, "bold"), bg='#f0f0f0')
        self.list_label.pack(anchor=tk.W, pady=(0, 5))
        
        # Listbox with scrollbar
        self.list_frame = tk.Frame(self.left_panel)
        self.list_frame.pack(fill=tk.BOTH, expand=True)
        
        self.place_listbox = tk.Listbox(self.list_frame, height=15, font=("Helvetica", 10),
                                       selectmode=tk.SINGLE, activestyle='dotbox')
        self.scrollbar = tk.Scrollbar(self.list_frame, orient=tk.VERTICAL)
        
        self.place_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.place_listbox.yview)
        
        self.place_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.place_listbox.bind("<<ListboxSelect>>", self.on_select)
        
        # Right panel for details
        self.right_panel = tk.Frame(self.content_frame, bg='#ffffff', relief=tk.RAISED, bd=1)
        self.right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Place details
        self.details_frame = tk.Frame(self.right_panel, bg='#ffffff')
        self.details_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        self.place_label = tk.Label(self.details_frame, text="Select a place to view details", 
                                  font=("Helvetica", 18, "bold"), bg='#ffffff', fg='#2c3e50')
        self.place_label.pack(pady=(0, 15))
        
        self.image_label = tk.Label(self.details_frame, bg='#ffffff')
        self.image_label.pack(pady=(0, 10))
        
        # Add map link button
        self.map_link_button = tk.Button(self.details_frame, text="🗺️ View on Map", 
                                        font=("Helvetica", 12), 
                                        bg="#4CAF50", fg="white",
                                        cursor="hand2",
                                        command=self.open_map_link,
                                        state=tk.DISABLED,
                                        relief=tk.FLAT,
                                        padx=20, pady=8)
        self.map_link_button.pack(pady=(0, 15))
        
        # Description with scrollable text - MADE READ-ONLY
        self.desc_frame = tk.Frame(self.details_frame, bg='#ffffff')
        self.desc_frame.pack(fill=tk.BOTH, expand=True)
        
        self.desc_text = scrolledtext.ScrolledText(self.desc_frame, wrap=tk.WORD, 
                                                 font=("Helvetica", 11), height=8,
                                                 bg='#f8f9fa', relief=tk.FLAT, bd=5,
                                                 state=tk.DISABLED)  # ALWAYS READ-ONLY
        self.desc_text.pack(fill=tk.BOTH, expand=True)
        
        # Statistics frame
        self.stats_frame = tk.Frame(self.places_frame, bg='#f0f0f0')
        self.stats_frame.pack(fill=tk.X, pady=(15, 0))
        
        self.stats_label = tk.Label(self.stats_frame, text="", font=("Helvetica", 10), 
                                  bg='#f0f0f0', fg='#7f8c8d')
        self.stats_label.pack()

    def setup_info_tab(self):
        """Setup the travel information tab"""
        # Title for info tab
        info_title = tk.Label(self.info_frame, text="🧳 Cambodia Travel Information 🧳", 
                             font=("Helvetica", 18, "bold"), bg='#f0f0f0', fg='#2c3e50')
        info_title.pack(pady=(10, 20))
        
        # Create frame for buttons and content
        info_content_frame = tk.Frame(self.info_frame, bg='#f0f0f0')
        info_content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Left panel for category buttons
        button_frame = tk.Frame(info_content_frame, bg='#f0f0f0', width=220)
        button_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        button_frame.pack_propagate(False)
        
        # Category buttons - UPDATED to remove budget/safety and add activities
        categories = [
            ("🏞️ Waterfalls", "waterfalls"),
            ("🐘 Wildlife", "wildlife"), 
            ("🎨 Crafts", "crafts"),
            ("🍽️ Food", "food"),
            ("🌊 Water Sports", "water_sports"),
            ("🏔️ Land Adventures", "land_adventures")
        ]
        
        self.info_buttons = {}
        for display_name, category in categories:
            btn = tk.Button(button_frame, text=display_name,
                          font=("Helvetica", 11),
                          bg="#3498db", fg="white",
                          relief=tk.FLAT, padx=15, pady=8,
                          cursor="hand2",
                          command=lambda cat=category: self.show_travel_info(cat))
            btn.pack(fill=tk.X, pady=2)
            self.info_buttons[category] = btn
        
        # Activity search section
        search_frame = tk.Frame(button_frame, bg='#f0f0f0')
        search_frame.pack(fill=tk.X, pady=(20, 0))
        
        search_label = tk.Label(search_frame, text="🔍 Search Activities:", 
                               font=("Helvetica", 10, "bold"), bg='#f0f0f0')
        search_label.pack(anchor=tk.W)
        
        self.activity_search_var = tk.StringVar()
        activity_search_entry = tk.Entry(search_frame, textvariable=self.activity_search_var,
                                       font=("Helvetica", 10))
        activity_search_entry.pack(fill=tk.X, pady=(5, 5))
        
        search_btn = tk.Button(search_frame, text="Search",
                             font=("Helvetica", 10),
                             bg="#e74c3c", fg="white",
                             relief=tk.FLAT, pady=5,
                             command=self.search_travel_activities)
        search_btn.pack(fill=tk.X)
        
        # Clear search button
        clear_btn = tk.Button(search_frame, text="Clear",
                             font=("Helvetica", 10),
                             bg="#95a5a6", fg="white",
                             relief=tk.FLAT, pady=5,
                             command=self.clear_activity_search)
        clear_btn.pack(fill=tk.X, pady=(2, 0))
        
        # Show All Activities button
        all_activities_btn = tk.Button(search_frame, text="Show All Activities",
                                     font=("Helvetica", 10),
                                     bg="#9b59b6", fg="white",
                                     relief=tk.FLAT, pady=5,
                                     command=self.show_all_activities)
        all_activities_btn.pack(fill=tk.X, pady=(2, 0))
        
        # Right panel for info display
        info_display_frame = tk.Frame(info_content_frame, bg='#ffffff', relief=tk.RAISED, bd=1)
        info_display_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Info text area - MADE READ-ONLY
        self.info_text = scrolledtext.ScrolledText(info_display_frame, wrap=tk.WORD,
                                                  font=("Helvetica", 11),
                                                  bg='#f8f9fa', relief=tk.FLAT, bd=10,
                                                  state=tk.DISABLED)  # ALWAYS READ-ONLY
        self.info_text.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Read-only notice
        notice_label = tk.Label(info_display_frame, 
                               text="📌 Travel information is read-only to prevent accidental changes",
                               font=("Helvetica", 9, "italic"), 
                               bg='#ffffff', fg='#7f8c8d')
        notice_label.pack(pady=(0, 10))
        
        # Show initial info
        self.show_travel_info("waterfalls")

    def show_travel_info(self, category):
        """Display travel information for selected category"""
        try:
            # Reset button colors
            for btn in self.info_buttons.values():
                btn.config(bg="#3498db")
            
            # Highlight selected button
            if category in self.info_buttons:
                self.info_buttons[category].config(bg="#2980b9")
            
            # Get and display info based on category
            if category == "water_sports":
                info_text = self.format_activities_info("water_sports")
            elif category == "land_adventures":
                info_text = self.format_activities_info("land_adventures")
            else:
                info_text = format_travel_info(category)
            
            # Temporarily enable text widget to update content
            self.info_text.config(state=tk.NORMAL)
            self.info_text.delete(1.0, tk.END)
            self.info_text.insert(1.0, info_text)
            self.info_text.config(state=tk.DISABLED)  # Make read-only again
            
        except Exception as e:
            messagebox.showerror("Info Error", f"Error displaying travel info: {e}")

    def format_activities_info(self, activity_type):
        """Format activities information for display"""
        if activity_type == "water_sports":
            info_text = "🌊 WATER SPORTS IN CAMBODIA 🌊\n\n"
            activities = get_activities_by_type("water_sports")
        elif activity_type == "land_adventures":
            info_text = "🏔️ LAND ADVENTURES IN CAMBODIA 🏔️\n\n"
            activities = get_activities_by_type("land_adventures")
        else:
            return "No activities found for this category."
        
        for activity, details in activities.items():
            info_text += f"• {activity}\n"
            if isinstance(details.get('locations'), list):
                locations = ", ".join(details['locations'])
            else:
                locations = details.get('locations', 'Various locations')
            
            info_text += f"  📍 Locations: {locations}\n"
            info_text += f"  📊 Difficulty: {details.get('difficulty', 'N/A')}\n"
            info_text += f"  📅 Best Season: {details.get('season', 'N/A')}\n\n"
        
        return info_text

    def search_travel_activities(self):
        """Search for activities based on keyword"""
        keyword = self.activity_search_var.get().strip()
        if not keyword:
            messagebox.showinfo("Search", "Please enter a search keyword")
            return
        
        try:
            results = search_activities(keyword)
            
            if results:
                search_text = f"🔍 SEARCH RESULTS FOR: '{keyword.upper()}' 🔍\n\n"
                for activity, info in results.items():
                    search_text += f"• {activity}\n"
                    if isinstance(info, dict):
                        if isinstance(info.get('locations'), list):
                            locations = ", ".join(info['locations'])
                        else:
                            locations = info.get('locations', 'Various locations')
                        
                        search_text += f"  📍 Locations: {locations}\n"
                        search_text += f"  📊 Difficulty: {info.get('difficulty', 'N/A')}\n"
                        search_text += f"  📅 Season: {info.get('season', 'N/A')}\n"
                    search_text += "\n"
                
                # Temporarily enable text widget to update content
                self.info_text.config(state=tk.NORMAL)
                self.info_text.delete(1.0, tk.END)
                self.info_text.insert(1.0, search_text)
                self.info_text.config(state=tk.DISABLED)  # Make read-only again
            else:
                # Temporarily enable text widget to update content
                self.info_text.config(state=tk.NORMAL)
                self.info_text.delete(1.0, tk.END)
                self.info_text.insert(1.0, f"❌ No activities found for keyword: '{keyword}'\n\n💡 Try searching for:\n• beginner, intermediate, advanced\n• water, climbing, biking, trekking\n• river, mountain, coast, temple\n• kayaking, diving, climbing, zipline")
                self.info_text.config(state=tk.DISABLED)  # Make read-only again
                
        except Exception as e:
            messagebox.showerror("Search Error", f"Error searching activities: {e}")

    def show_all_activities(self):
        """Show all available activities"""
        try:
            all_activities = get_all_available_activities()
            
            if all_activities:
                activities_text = "🎯 ALL AVAILABLE ACTIVITIES IN CAMBODIA 🎯\n\n"
                
                # Separate water sports and land adventures
                water_sports = {}
                land_adventures = {}
                
                for activity, info in all_activities.items():
                    if activity.startswith("Water Sport:"):
                        water_sports[activity] = info
                    elif activity.startswith("Land Adventure:"):
                        land_adventures[activity] = info
                
                # Display water sports
                if water_sports:
                    activities_text += "🌊 WATER SPORTS:\n" + "-" * 40 + "\n"
                    for activity, info in water_sports.items():
                        activities_text += f"• {activity.replace('Water Sport: ', '')}\n"
                        if isinstance(info.get('locations'), list):
                            locations = ", ".join(info['locations'])
                        else:
                            locations = info.get('locations', 'Various locations')
                        activities_text += f"  📍 Locations: {locations}\n"
                        activities_text += f"  📊 Difficulty: {info.get('difficulty', 'N/A')}\n"
                        activities_text += f"  📅 Season: {info.get('season', 'N/A')}\n\n"
                
                # Display land adventures
                if land_adventures:
                    activities_text += "🏔️ LAND ADVENTURES:\n" + "-" * 40 + "\n"
                    for activity, info in land_adventures.items():
                        activities_text += f"• {activity.replace('Land Adventure: ', '')}\n"
                        if isinstance(info.get('locations'), list):
                            locations = ", ".join(info['locations'])
                        else:
                            locations = info.get('locations', 'Various locations')
                        activities_text += f"  📍 Locations: {locations}\n"
                        activities_text += f"  📊 Difficulty: {info.get('difficulty', 'N/A')}\n"
                        activities_text += f"  📅 Season: {info.get('season', 'N/A')}\n\n"
                
                activities_text += "💡 SEARCH TIPS:\n" + "-" * 40 + "\n"
                activities_text += "Use the search box above to find activities by:\n"
                activities_text += "• Difficulty: 'beginner', 'intermediate', 'advanced'\n"
                activities_text += "• Type: 'water', 'climbing', 'biking', 'trekking'\n"
                activities_text += "• Location: 'river', 'mountain', 'coast', 'temple'\n"
                activities_text += "• Season: 'year-round', specific months\n"
                
                # Reset button colors first
                for btn in self.info_buttons.values():
                    btn.config(bg="#3498db")
                
                # Temporarily enable text widget to update content
                self.info_text.config(state=tk.NORMAL)
                self.info_text.delete(1.0, tk.END)
                self.info_text.insert(1.0, activities_text)
                self.info_text.config(state=tk.DISABLED)  # Make read-only again
            else:
                messagebox.showinfo("Activities", "No activities data available")
                
        except Exception as e:
            messagebox.showerror("Activities Error", f"Error loading activities: {e}")

    def clear_activity_search(self):
        """Clear the activity search field and show waterfalls info"""
        self.activity_search_var.set("")
        self.show_travel_info("waterfalls")

    def load_places(self, filepath):
        """Load places from CSV file with enhanced error handling"""
        places = []
        try:
            if not os.path.exists(filepath):
                messagebox.showerror("File Error", f"CSV file not found: {filepath}")
                return places
                
            with open(filepath, newline='', encoding="windows-1252") as file:
                reader = csv.reader(file)
                row_num = 0
                for row in reader:
                    row_num += 1
                    if len(row) >= 3:
                        name = row[0].strip()
                        img_relative_path = row[1].strip()
                        desc = row[2].strip()
                        
                        # Handle additional columns if present
                        additional_info = {}
                        map_url = ""
                        if len(row) > 3:
                            map_url = row[3].strip()
                            additional_info['category'] = row[4].strip() if len(row) > 4 else ""
                            additional_info['location'] = row[5].strip() if len(row) > 5 else ""
                        
                        img_path = os.path.join(script_dir, img_relative_path)
                        places.append((name, img_path, desc, map_url, additional_info))
                    else:
                        print(f"Warning: Row {row_num} has insufficient columns: {row}")
                        
        except Exception as e:
            messagebox.showerror("Loading Error", f"Error loading places: {e}")
            
        return places

    def update_list(self, *args):
        """Update the listbox based on search term"""
        search_term = self.search_var.get().lower()
        self.filtered_places = [place for place in self.places 
                              if search_term in place[0].lower() or 
                              (len(place) > 4 and search_term in str(place[4]).lower())]

        self.place_listbox.delete(0, tk.END)
        for i, place in enumerate(self.filtered_places):
            # Add category indicator if available
            display_name = place[0]
            if len(place) > 4 and place[4].get('category'):
                display_name += f" ({place[4]['category']})"
            self.place_listbox.insert(tk.END, display_name)

        self.update_stats()
        
        # Auto-select first item if search results exist
        if self.filtered_places:
            self.place_listbox.selection_set(0)
            self.index = 0
            self.show_place()
        else:
            self.clear_display()

    def on_select(self, event):
        """Handle listbox selection"""
        try:
            selection = self.place_listbox.curselection()
            if selection:
                self.index = selection[0]
                self.show_place()
        except Exception as e:
            messagebox.showerror("Selection Error", f"An error occurred: {e}")

    def show_place(self):
        """Display selected place information"""
        try:
            if not self.filtered_places or self.index >= len(self.filtered_places):
                return
                
            place_info = self.filtered_places[self.index]
            name, image_path, desc = place_info[0], place_info[1], place_info[2]
            map_url = place_info[3] if len(place_info) > 3 else ""
            additional_info = place_info[4] if len(place_info) > 4 else {}
            
            # Store current map URL and update button state
            self.current_map_url = map_url
            if map_url:
                self.map_link_button.config(state=tk.NORMAL)
            else:
                self.map_link_button.config(state=tk.DISABLED)
            
            # Update place name
            self.place_label.config(text=name)
            
            # Load and display image
            self.load_image(image_path)
            
            # Update description
            full_desc = desc
            
            # Add additional information if available
            if additional_info:
                if additional_info.get('location'):
                    full_desc += f"\n\n📍 Location: {additional_info['location']}"
                if additional_info.get('category'):
                    full_desc += f"\n🏷️ Category: {additional_info['category']}"
            
            # Temporarily enable text widget to update content
            self.desc_text.config(state=tk.NORMAL)
            self.desc_text.delete(1.0, tk.END)
            self.desc_text.insert(1.0, full_desc)
            self.desc_text.config(state=tk.DISABLED)  # Make read-only again
            
        except Exception as e:
            messagebox.showerror("Display Error", f"An error occurred while displaying place: {e}")

    def load_image(self, image_path):
        """Load and display image with better error handling"""
        try:
            if os.path.exists(image_path):
                img = Image.open(image_path)
                
                # Calculate aspect ratio and resize accordingly
                img_width, img_height = img.size
                aspect_ratio = img_width / img_height
                
                if aspect_ratio > (IMAGE_WIDTH / IMAGE_HEIGHT):
                    new_width = IMAGE_WIDTH
                    new_height = int(IMAGE_WIDTH / aspect_ratio)
                else:
                    new_height = IMAGE_HEIGHT
                    new_width = int(IMAGE_HEIGHT * aspect_ratio)
                
                img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                self.image_label.config(image=photo)
                self.image_label.image = photo
            else:
                # Show placeholder for missing image
                self.show_placeholder_image()
                
        except Exception as e:
            self.show_placeholder_image()
            print(f"Image loading error: {e}")

    def show_placeholder_image(self):
        """Show a placeholder when image is not available"""
        # Create a simple placeholder image
        placeholder = Image.new('RGB', (IMAGE_WIDTH, IMAGE_HEIGHT), color='#ecf0f1')
        photo = ImageTk.PhotoImage(placeholder)
        self.image_label.config(image=photo)
        self.image_label.image = photo

    def clear_display(self):
        """Clear the display when no places are found"""
        self.place_label.config(text="No places found")
        
        # Temporarily enable text widget to update content
        self.desc_text.config(state=tk.NORMAL)
        self.desc_text.delete(1.0, tk.END)
        self.desc_text.insert(1.0, "Try adjusting your search terms.")
        self.desc_text.config(state=tk.DISABLED)  # Make read-only again
        
        self.show_placeholder_image()

    def update_stats(self):
        """Update statistics display"""
        total_places = len(self.places)
        filtered_count = len(self.filtered_places)
        
        if self.search_var.get():                        
            stats_text = f"Showing {filtered_count} of {total_places} places"
        else:
            stats_text = f"Total places: {total_places}"
            
        self.stats_label.config(text=stats_text)

    def open_map_link(self):
        """Open the map URL in the default web browser"""
        if self.current_map_url:
            try:
                webbrowser.open(self.current_map_url)
            except Exception as e:
                messagebox.showerror("Browser Error", f"Could not open map link: {e}")
        else:
            messagebox.showinfo("No Map", "No map link available for this location.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TravelGuideApp(root)
    root.mainloop()