#
# Create players
#
import unreal

unreal.log('begin')
assetTools = unreal.AssetToolsHelpers.get_asset_tools()
EAL = unreal.EditorAssetLibrary()

for i in range(1, 13):
    playerName = f'MP_G{i}'
    textureName = f'MT_G{i}'
    unreal.log(f'create {playerName}')
    player = assetTools.create_asset(
                    playerName,
                    "/Game/Features/Multiplay/Test/",
                    unreal.MediaPlayer,
                    unreal.MediaPlayerFactoryNew(),
                )
    
    tex = assetTools.create_asset(
                    textureName,
                    "/Game/Features/Multiplay/Test/",
                    unreal.MediaTexture,
                    unreal.MediaTextureFactoryNew(),
                )
    #tex.media_player = player
    
unreal.log('end')