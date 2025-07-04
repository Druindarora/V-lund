import os
import sys

MODULES_BASE = os.path.join("Vølund", "src", "modules")
SUBFOLDERS = ["services", "ui", "db", "tests"]

def create_folder_with_init(path):
    os.makedirs(path, exist_ok=True)
    init_file = os.path.join(path, "__init__.py")
    open(init_file, "a").close()
    print(f"📁+🧩 {path}")

def create_module(module_name):
    module_path = os.path.join(MODULES_BASE, module_name)

    if os.path.exists(module_path):
        print(f"⚠️ Le module '{module_name}' existe déjà. Abandon.")
        return

    print(f"🚀 Création du module : {module_name}")
    create_folder_with_init(module_path)

    for sub in SUBFOLDERS:
        sub_path = os.path.join(module_path, sub)
        create_folder_with_init(sub_path)

    print(f"✅ Module '{module_name}' créé avec succès.")

def main():
    if not os.path.exists(MODULES_BASE):
        print(f"❌ Dossier introuvable : {MODULES_BASE}")
        return

    # Ligne de commande
    if len(sys.argv) > 1:
        module_name = sys.argv[1]
    else:
        module_name = input("🔤 Entrez le nom du module à créer : ").strip()

    if not module_name:
        print("❌ Aucun nom fourni. Abandon.")
        return

    create_module(module_name)

if __name__ == "__main__":
    main()
