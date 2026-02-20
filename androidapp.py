package com.example.littlelemonmenu

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.navigation.NavController
import androidx.navigation.NavType
import androidx.navigation.compose.*
import androidx.navigation.navArgument

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            LittleLemonApp()
        }
    }
}

/* ---------- Little Lemon Colors ---------- */
val LittleLemonGreen = Color(0xFF495E57)
val LittleLemonYellow = Color(0xFFF4CE14)

/* ---------- Data Model ---------- */
data class MenuItem(
    val id: Int,
    val title: String,
    val description: String,
    val price: String
)

/* ---------- Sample Menu Data ---------- */
val menuItems = listOf(
    MenuItem(1, "Greek Salad", "Fresh salad with feta cheese and olives", "$12"),
    MenuItem(2, "Bruschetta", "Grilled bread with garlic and tomatoes", "$8"),
    MenuItem(3, "Lemon Dessert", "Traditional lemon cake with sugar glaze", "$6")
)

/* ---------- App Navigation ---------- */
@Composable
fun LittleLemonApp() {
    val navController = rememberNavController()

    NavHost(navController = navController, startDestination = "menu") {
        composable("menu") {
            MenuScreen(navController)
        }
        composable(
            "details/{itemId}",
            arguments = listOf(navArgument("itemId") { type = NavType.IntType })
        ) { backStackEntry ->
            val itemId = backStackEntry.arguments?.getInt("itemId")
            val item = menuItems.first { it.id == itemId }
            DetailsScreen(item)
        }
    }
}

/* ---------- Menu Screen ---------- */
@Composable
fun MenuScreen(navController: NavController) {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp)
    ) {
        Text(
            text = "Little Lemon",
            fontSize = 28.sp,
            fontWeight = FontWeight.Bold,
            color = LittleLemonGreen
        )

        Spacer(modifier = Modifier.height(16.dp))

        LazyColumn {
            items(menuItems) { item ->
                Card(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(vertical = 8.dp)
                        .clickable {
                            navController.navigate("details/${item.id}")
                        },
                    colors = CardDefaults.cardColors(
                        containerColor = LittleLemonYellow
                    )
                ) {
                    Column(modifier = Modifier.padding(16.dp)) {
                        Text(
                            text = item.title,
                            fontSize = 20.sp,
                            fontWeight = FontWeight.Bold
                        )
                        Text(text = item.price)
                    }
                }
            }
        }
    }
}

/* ---------- Details Screen ---------- */
@Composable
fun DetailsScreen(item: MenuItem) {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp)
    ) {
        Text(
            text = item.title,
            fontSize = 26.sp,
            fontWeight = FontWeight.Bold,
            color = LittleLemonGreen
        )

        Spacer(modifier = Modifier.height(12.dp))

        Text(text = item.description, fontSize = 18.sp)
        Spacer(modifier = Modifier.height(8.dp))
        Text(text = "Price: ${item.price}", fontSize = 18.sp)
    }
}
